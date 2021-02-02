import logging
import requests
from get_token.token_service import TokenService
from variables import dict


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy dictionary-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.

# Metoda służy do wykonania żądania GET na końcówkę /v1/dictionary/countries
def get_countries():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    url = f"{base_api_uri}/v1/dictionary/countries"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for countries: url {url}, headers {headers}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/dictionary/disciplines
def get_disciplines():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    url = f"{base_api_uri}/v1/dictionary/disciplines"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for disciplines: url {url}, headers {headers}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/dictionary/languages
def get_languages():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    url = f"{base_api_uri}/v1/dictionary/languages"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for languages: url {url}, headers {headers}")
    return response.text
