import logging
import requests
from variables import dict
from get_token.token_service import TokenService


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy institution-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.


# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/page
def get_page_by_status():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('institution.page')
    size = dict.get('institution.size')
    status = dict.get('institution.status')
    url = f"{base_api_uri}/v1/institutions/page?page={page}&size={size}&status={status}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of institutions: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}, status = {status}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/polon/page
def get_page_polon():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('institution.page')
    size = dict.get('institution.size')
    url = f"{base_api_uri}/v1/institutions/polon/page?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of POLON institutions: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/polon/uid/{uid}
def get_metadata_by_polon_uid():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    uid = dict.get('institution.polon.uid')
    url = f"{base_api_uri}/v1/institutions/polon/uid/{uid}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of institution by POLON UID: url {url}, headers {headers}")
    logging.info(f"Params: uid = {uid}")
    return response.text

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/polon/{id}
def get_metadata_by_polon_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    polon_id = dict.get('institution.polon.id')
    url = f"{base_api_uri}/v1/institutions/polon/{polon_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of institution by POLON ID: url {url}, headers {headers}")
    logging.info(f"Params: id = {polon_id}")
    return response.text

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/version/{version}
def get_metadata_by_version():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    version = dict.get('institution.version')
    url = f"{base_api_uri}/v1/institutions/version/{version}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of institution by version: url {url}, headers {headers}")
    logging.info(f"Params: version = {version}")
    return response.text

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/{id}
def get_extended_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    institution_id = dict.get('institution.id')
    url = f"{base_api_uri}/v1/institutions/{institution_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for extended metadata of institution by id: url {url}, headers {headers}")
    logging.info(f"Params: id = {institution_id}")
    return response.text

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutions/{id}/metadata
def get_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    institution_id = dict.get('institution.id')
    url = f"{base_api_uri}/v1/institutions/{institution_id}/metadata"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of institution by id: url {url}, headers {headers}")
    logging.info(f"Params: id = {institution_id}")
    return response.text