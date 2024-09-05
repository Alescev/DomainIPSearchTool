# URLscanInternetFinder

This Python script performs a bulk search of domains using the urlscan.io API and Bing Search API.

## Features

- Retrieves domains from urlscan.io based on a user-provided query
- Searches for articles related to the found domains using Bing Search API
- Analyzes search results to find mentions of domains on other websites
- Verifies the presence of domains in article texts, considering various types of escaping
- Option to save results to a text file

## Requirements

- Python 3.x
- Libraries: `requests`, `python-dotenv`

## Configuration

Before running the script, make sure to configure the API keys:

1. Create a `.env` file in the same directory as the script
2. Add your API keys to the `.env` file in the following format:
   ```
   URLSCAN_API_KEY=your_urlscan_api_key_here
   BING_API_KEY=your_bing_api_key_here
   ```
3. Obtain API keys from:
   - [urlscan.io](https://urlscan.io/) for URLSCAN_API_KEY
   - [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) for BING_API_KEY

The script will automatically read the API keys from the `.env` file.

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

## Notes

This script is useful for large-scale intelligence research and domain analysis. Make sure to comply with the terms of service of the APIs used.

## Security

The `.env` file containing your API keys is included in the `.gitignore` file to prevent accidental exposure of sensitive information. Never commit or share your `.env` file.