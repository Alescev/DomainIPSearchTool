# URLscanInternetFinder

Questo script Python esegue una ricerca in massa di domini utilizzando l'API di urlscan.io e Bing Search.

## Funzionalità

- Recupera domini da urlscan.io basati su una query fornita dall'utente
- Cerca articoli relativi ai domini trovati utilizzando Bing Search API
- Analizza i risultati della ricerca per trovare menzioni dei domini in altri siti web
- Verifica la presenza dei domini nei testi degli articoli, considerando vari tipi di escaping

## Requisiti

- Python 3.x
- Librerie: `requests`

## Configurazione

Prima di eseguire lo script, assicurati di configurare le seguenti API key:

1. URLSCAN_API_KEY: Ottieni una chiave API da [urlscan.io](https://urlscan.io/)
2. BING_API_KEY: Ottieni una chiave API da [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api)

Inserisci le tue chiavi API nelle variabili corrispondenti all'inizio dello script.

## Utilizzo

1. Esegui lo script: `python bulk_search.py`
2. Inserisci la query di ricerca quando richiesto
3. Lo script mostrerà i domini trovati e gli articoli correlati per ciascun dominio

## Output

Per ogni dominio trovato, lo script visualizzerà:
- Titolo dell'articolo
- Snippet dell'articolo
- URL dell'articolo

Verranno mostrati solo gli articoli in cui il dominio è menzionato nel testo.

## Note

Questo script è utile per ricerche di intelligence e analisi di domini su larga scala. Assicurati di rispettare i termini di servizio delle API utilizzate.