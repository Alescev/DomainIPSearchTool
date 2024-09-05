import os
from dotenv import load_dotenv
import requests
from urllib.parse import quote_plus
import re

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
URLSCAN_API_KEY = os.getenv('URLSCAN_API_KEY')
BING_API_KEY = os.getenv('BING_API_KEY')

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
    # Create a regex to search for the domain with various types of escaping
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
        print(f"Regex error: {e}")
        return False

def save_results_to_file(parsed_results, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for domain, articles in parsed_results.items():
            f.write(f"Articles found for {domain}:\n")
            f.write("=" * 80 + "\n")
            for article in articles:
                if check_domain_in_text(domain, article['snippet']):
                    f.write(f"Title  : {article['title']}\n")
                    f.write(f"Snippet: {article['snippet']}\n")
                    f.write(f"URL    : {article['url']}\n")
                    f.write("-" * 80 + "\n")
            f.write("\n")

def main():
    query = input("Enter the urlscan query: ")
    domains = get_domains_from_urlscan(query)
    print(f"\nDomains found: {domains}\n")
    search_results = search_articles_for_domains(domains)
    parsed_results = parse_search_results(search_results)
    
    for domain, articles in parsed_results.items():
        print(f"Articles found for {domain}:")
        print("=" * 80)
        for article in articles:
            if check_domain_in_text(domain, article['snippet']):
                print(f"Title  : {article['title']}")
                print(f"Snippet: {article['snippet']}")
                print(f"URL    : {article['url']}")
                print("-" * 80)
        print("\n")
    
    save_option = input("Do you want to save the results to a file? (y/n): ").lower()
    if save_option == 'y':
        filename = input("Enter the filename to save results (e.g., results.txt): ")
        save_results_to_file(parsed_results, filename)
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()