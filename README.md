# 🔍 Bulk Domain and IP Search Tool

This Python script is designed to assist in cyber threat intelligence analysis and research activities. It searches for domains/IPs from various sources and finds related articles.

## 🚀 Features

- Retrieves domains/IPs from multiple sources:
  - 🌐 urlscan.io
  - 🔎 FOFA
  - 🌍 Censys
  - 🖧 Shodan
- Searches for articles related to the found domains/IPs using:
  - 🔍 Bing Search API
  - 🔎 Google Custom Search API
- Analyzes search results to find mentions of domains/IPs on other websites
- Verifies the presence of domains/IPs in article texts, considering various escaping techniques
- Option to save results to a text file

## 🛠️ Requirements

- Python 3.x
- Libraries: `requests`, `python-dotenv`

## ⚙️ Configuration

1. Create a `.env` file in the same directory as the script
2. Add your API keys to the `.env` file:
   ```
   URLSCAN_API_KEY=your_urlscan_api_key_here
   BING_API_KEY=your_bing_api_key_here
   FOFA_API_KEY=your_fofa_email:your_fofa_key_here
   CENSYS_API_KEY=your_censys_api_id:your_censys_api_secret_here
   SHODAN_API_KEY=your_shodan_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_SEARCH_ENGINE_ID=your_google_search_engine_id_here
   RESULT_LIMIT=100
   ```

## 🚀 Usage

Run the script with the following command:

```
python bulk_search.py [query] [options]
```

### Parameters

- `query`: The search query to use for finding domains/IPs (optional if `-t` is used)
- `-t`, `--targets`: Comma-separated list of domains or IP addresses to search for
- `-u`, `--urlscan`: Use URLscan as a source
- `-f`, `--fofa`: Use FOFA as a source
- `-c`, `--censys`: Use Censys as a source
- `-s`, `--shodan`: Use Shodan as a source
- `-b`, `--bing`: Use Bing for article search
- `-g`, `--google`: Use Google for article search
- `-o`, `--output`: Filename to save results (e.g., results.txt)

### Examples

1. Search for a specific query using URLscan, then search for articles using Bing:
   ```
   python bulk_search.py "query" -u -b
   ```

<img width="513" alt="example_1" src="https://github.com/user-attachments/assets/c9b440d4-2fc2-4e62-ac9e-602d6941a09c">


2. Search for articles about specific targets using Google and save results:
   ```
   python bulk_search.py -t example.com,192.168.1.1 -g -o results.txt
   ```
<img width="846" alt="example_2" src="https://github.com/user-attachments/assets/62bf9212-7cc0-47dd-b8f1-5facd1acb5e7">

3. Search for IPs related to a query using Censys and Shodan, then search for articles using Bing:
   ```
   python bulk_search.py "apache server" -c -s -b
   ```

## 📊 Output

For each found domain/IP, the script will display:
- Article title
- Article snippet
- Article URL

Only articles with confirmed mentions of the domain/IP are shown.

If an output file is specified, the results will be saved in the following format:

   ```
Articles found for example.com:
================================================================================
Title : Example Article Title
Snippet: This is a snippet of the article mentioning example.com...
URL : https://example-article-url.com
--------------------------------------------------------------------------------
   ```

## ⚠️ Notes

- At least one source (-u, -f, -c, -s) must be specified when using a query.
- Either a query or targets (-t) must be specified.
- Only one search engine (-b or -g) can be used at a time.
- The RESULT_LIMIT in the .env file determines the maximum number of results fetched from each source.
