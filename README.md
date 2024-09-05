# URLscanInternetFinder

This Python script performs a bulk search of domains using the urlscan.io API and Bing Search.

## Features

- Retrieves domains from urlscan.io based on a user-provided query
- Searches for articles related to the found domains using Bing Search API
- Analyzes search results to find mentions of domains on other websites
- Verifies the presence of domains in article texts, considering various types of escaping
- Option to save results to a text file

## Requirements

- Python 3.x
- Libraries: `requests`

## Configuration

Before running the script, make sure to configure the following API keys:

1. URLSCAN_API_KEY: Obtain an API key from [urlscan.io](https://urlscan.io/)
2. BING_API_KEY: Obtain an API key from [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api)

Insert your API keys into the corresponding variables at the beginning of the script.

## Usage

1. Run the script: `python bulk_search.py`
2. Enter the search query when prompted
3. The script will display the found domains and related articles for each domain
4. Choose whether to save the results to a file

## Output

For each found domain, the script will display:
- Article title
- Article snippet
- Article URL

Only articles where the domain is mentioned in the text will be shown.

If you choose to save the results, they will be written to a text file in a similar format.

## Notes

This script is useful for large-scale intelligence research and domain analysis. Make sure to comply with the terms of service of the APIs used.