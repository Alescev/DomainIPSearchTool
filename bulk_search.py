import requests
from urllib.parse import quote_plus
import re

# Configura la tua API key di urlscan e Bing Search
URLSCAN_API_KEY = 'apikey'
BING_API_KEY = 'apikey'

def get_domains_from_urlscan(query):
    url = 'https://urlscan.io/api/v1/search/'
    headers = {
        'API-Key': URLSCAN_API_KEY
    }
    params = {
        'q': query
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    results = response.json().get('results', [])
    domains = [result['page']['domain'] for result in results]
    return domains

def search_articles_for_domains(domains):
    search_results = {}
    headers = {
        'Ocp-Apim-Subscription-Key': BING_API_KEY
    }
    for domain in domains:
        query = quote_plus(f'"{domain}"')
        search_url = f'https://api.bing.microsoft.com/v7.0/search?q={query}'
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        search_results[domain] = response.json()
    return search_results

def parse_search_results(search_results):
    parsed_results = {}
    for domain, results in search_results.items():
        articles = []
        for result in results.get('webPages', {}).get('value', []):
            article_domain = re.search(r'https?://([^/]+)', result.get('url')).group(1)
            if article_domain != domain:
                title = result.get('name')
                snippet = result.get('snippet')
                url = result.get('url')
                articles.append({'title': title, 'snippet': snippet, 'url': url})
        parsed_results[domain] = articles
    return parsed_results

def check_domain_in_text(domain, text):
    # Crea una regex per cercare il dominio con vari tipi di escaping
    escaped_domain = re.escape(domain)
    patterns = [
        escaped_domain,
        escaped_domain.replace(r'\.', r'\[dot\]'),
        escaped_domain.replace(r'\.', r'\(dot\)'),
        escaped_domain.replace(r'\.', r'\s*\.\s*')
    ]
    combined_pattern = '|'.join(patterns)
    try:
        return re.search(combined_pattern, text, re.IGNORECASE) is not None
    except re.error as e:
        print(f"Errore nella regex: {e}")
        return False

def main():
    query = input("Inserisci la query di urlscan: ")
    domains = get_domains_from_urlscan(query)
    print(f"\nDomini trovati: {domains}\n")
    search_results = search_articles_for_domains(domains)
    parsed_results = parse_search_results(search_results)
    for domain, articles in parsed_results.items():
        print(f"Articoli trovati per {domain}:")
        print("=" * 80)
        for article in articles:
            if check_domain_in_text(domain, article['snippet']):
                print(f"Titolo : {article['title']}")
                print(f"Snippet: {article['snippet']}")
                print(f"URL    : {article['url']}")
                print("-" * 80)
        print("\n")

if __name__ == "__main__":
    main()