import logging
import requests
from variables import dict
from get_token.token_service import TokenService


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy journals-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.


# Metoda służy do wykonania żądania GET na końcówkę /v1/journals/mnisw/page
def get_page_mnisw():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('journals.page')
    size = dict.get('journals.size')
    url = f"{base_api_uri}/v1/journals/mnisw/page?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of MNiSW journals: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/journals/page
def get_page_by_status():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('journals.page')
    size = dict.get('journals.size')
    status = dict.get('journals.status')
    url = f"{base_api_uri}/v1/journals/page?page={page}&size={size}&status={status}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of journals: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}, status = {status}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/journals/version/{version}
def get_metadata_by_version():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    version = dict.get('journals.version')
    url = f"{base_api_uri}/v1/journals/version/{version}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of journal by version: url {url}, headers {headers}")
    logging.info(f"Query params: version = {version}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/journals/{journalId}
def get_extended_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    journal_id = dict.get('journals.journalId')
    url = f"{base_api_uri}/v1/journals/{journal_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for extended metadata of journal by id: url {url}, headers {headers}")
    logging.info(f"Query params: journalId = {journal_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/journals/{journalId}/metadata
def get_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    journal_id = dict.get('journals.journalId')
    url = f"{base_api_uri}/v1/journals/{journal_id}/metadata"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of journal by id: url {url}, headers {headers}")
    logging.info(f"Query params: journalId = {journal_id}")
    return response.text
