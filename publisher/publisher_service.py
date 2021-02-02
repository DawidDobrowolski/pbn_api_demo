import logging
import requests
from variables import dict
from get_token.token_service import TokenService


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy publishers-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/{publisherId}
def get_extended_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    publisher_id = dict.get('publishers.publisherId')
    url = f"{base_api_uri}/v1/publishers/{publisher_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for extended metadata of publisher by id: url {url}, headers {headers}")
    logging.info(f"Params: publisherId = {publisher_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/{publisherId}/metadata
def get_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    publisher_id = dict.get('publishers.publisherId')
    url = f"{base_api_uri}/v1/publishers/{publisher_id}/metadata"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of publisher by id: url {url}, headers {headers}")
    logging.info(f"Params: publisherId = {publisher_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/mnisw/page
def get_page_mnisw():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('publishers.page')
    size = dict.get('publishers.size')
    url = f"{base_api_uri}/v1/publishers/mnisw/page?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of MNiSW publishers: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/mnisw/page/yearlist
def get_page_mnisw_year_list():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('publishers.page')
    size = dict.get('publishers.size')
    url = f"{base_api_uri}/v1/publishers/mnisw/page/yearlist?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of MNiSW publishers with points: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/page
def get_page_by_status():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('publishers.page')
    size = dict.get('publishers.size')
    status = dict.get('publishers.status')
    url = f"{base_api_uri}/v1/publishers/page?page={page}&size={size}&status={status}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of publishers: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}, status = {status}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publishers/version/{version}
def get_metadata_by_version():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    version = dict.get('publishers.version')
    url = f"{base_api_uri}/v1/publishers/version/{version}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of publisher by version: url {url}, headers {headers}")
    logging.info(f"Params: version = {version}")
    return response.text
