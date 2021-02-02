import logging
import requests
from variables import dict
from get_token.token_service import TokenService


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy person-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/{id}
def get_extended_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    person_id = dict.get('person.id')
    url = f"{base_api_uri}/v1/person/{person_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for extended metadata of person by id: url {url}, headers {headers}")
    logging.info(f"Params: id = {person_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/institution/{id}
def get_employees_by_institution_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    institution_id = dict.get('person.institution.id')
    url = f"{base_api_uri}/v1/person/institution/{institution_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of person by institution id: url {url}, headers {headers}")
    logging.info(f"Params: id = {institution_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/natural/{id}
def get_metadata_natural_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    natural_id = dict.get('person.natural.id')
    url = f"{base_api_uri}/v1/person/natural/{natural_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of person by natural id: url {url}, headers {headers}")
    logging.info(f"Params: id = {natural_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/page
def get_page_by_status():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('person.page')
    size = dict.get('person.size')
    status = dict.get('person.status')
    url = f"{base_api_uri}/v1/person/page?page={page}&size={size}&status={status}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of persons: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}, status = {status}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/polon/{uid}
def get_metadata_by_polon_uid():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    uid = dict.get('person.polon.uid')
    url = f"{base_api_uri}/v1/person/polon/{uid}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of person by POLON UID: url {url}, headers {headers}")
    logging.info(f"Params: uid = {uid}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/person/version/{version}
def get_metadata_by_version():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    version = dict.get('person.version')
    url = f"{base_api_uri}/v1/person/version/{version}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of person by version: url {url}, headers {headers}")
    logging.info(f"Params: version = {version}")
    return response.text
