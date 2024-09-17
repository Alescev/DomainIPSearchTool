# 🔍 Bulk Domain and IP Search Tool

This Python script is designed to assist in cyber threat intelligence analysis and research activities. 🕵️‍♀️💻

## 🚀 Features

- Retrieves domains/IPs from multiple sources:
  - 🌐 urlscan.io
  - 🔎 FOFA
  - 🌍 Censys
  - 🖧 Shodan
  - ⌨️ Direct input
- Searches for articles related to the found domains/IPs using:
  - 🔍 Bing Search API
  - 🔎 Google Custom Search API
- 🧐 Analyzes search results to find mentions of domains/IPs on other websites
- ✅ Verifies the presence of domains/IPs in article texts, considering various escaping techniques
- 💾 Option to save results to a text file

## 🎯 Use Cases in Cyber Threat Intelligence

1. 🚀 **Efficient Data Gathering**: Quickly collect information on multiple domains or IPs from various sources.
2. 🧩 **Context Enrichment**: Find existing research and articles mentioning your targets, providing additional context.
3. ⏱️ **Time-Saving**: Automate the process of searching multiple sources and analyzing results.
4. 🌐 **Comprehensive Coverage**: Leverage multiple data sources and search engines for a broader view.
5. 🔍 **Result Verification**: Automatically check if the domain/IP is mentioned in the article text, reducing false positives.

## 🛠️ Requirements

- 🐍 Python 3.x
- 📚 Libraries: `requests`, `python-dotenv`

## ⚙️ Configuration

Before running the script, configure the API keys:

1. 📁 Create a `.env` file in the same directory as the script
2. 🔑 Add your API keys to the `.env` file in the following format:
   ```
   URLSCAN_API_KEY=your_urlscan_api_key_here
   BING_API_KEY=your_bing_api_key_here
   FOFA_API_KEY=your_fofa_api_key_here
   CENSYS_API_KEY=your_censys_api_key_here
   SHODAN_API_KEY=your_shodan_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_SEARCH_ENGINE_ID=your_google_search_engine_id_here
   RESULT_LIMIT=100
   ```
3. 🔐 Obtain API keys from:
   - [urlscan.io](https://urlscan.io/) for URLSCAN_API_KEY
   - [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) for BING_API_KEY
   - [FOFA](https://fofa.info/) for FOFA_API_KEY
   - [Censys](https://censys.io/) for CENSYS_API_KEY
   - [Shodan](https://www.shodan.io/) for SHODAN_API_KEY
   - [Google Custom Search API](https://developers.google.com/custom-search/v1/overview) for GOOGLE_API_KEY and GOOGLE_SEARCH_ENGINE_ID

The script will automatically read the API keys and settings from the `.env` file.

## 🚀 Usage

1. 🖥️ Run the script: `python bulk_search.py`
2. 🔢 Select the search source (URLScan, FOFA, Censys, Shodan, or Direct Input)
3. 🔤 Enter the search query or domains/IPs when prompted
4. 🔍 Choose the search engine for articles (Bing or Google)
5. 👀 Review the displayed results
6. 💾 Optionally save the results to a file

## 📊 Output

For each found domain/IP, the script will display:
- 📌 Article title
- 📝 Article snippet
- 🔗 Article URL

Only articles with confirmed mentions of the domain/IP are shown. 👍

## Examples
- Example 1
![example_1](https://github.com/user-attachments/assets/4fcf8312-2246-4cb6-b859-ba9bb596abd9)
- Example 2
![example_2](https://github.com/user-attachments/assets/248a21b9-1543-4c9e-82b8-e9addeb9f278)
- Example 3
![example_3](https://github.com/user-attachments/assets/7097c376-2ce6-4ff0-934d-ee52d077b100)
- Example 4
![example_4](https://github.com/user-attachments/assets/c2edd99e-ac8a-4bbd-9a7e-cd649407ac31)

