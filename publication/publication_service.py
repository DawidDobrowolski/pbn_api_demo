import logging
import requests
from variables import dict
from get_token.token_service import TokenService


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy publications-controller (żądania typu GET i POST).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers, przy której podane szczegółowe informacje o tych nagłówkach.
# W przypadku żądań POST dołączane jest ciało typu json, wprowadzone przez użytkownika na stronie aplikacji demo.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.


# Metoda służy do wykonania żądania GET na końcówkę /v1/publications/{publicationId}/metadata
def get_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    publication_id = dict.get('publications.publicationId')
    url = f"{base_api_uri}/v1/publications/{publication_id}/metadata"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of publication by id: url {url}, headers {headers}")
    logging.info(f"Params: publicationId = {publication_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publications/doi
def get_metadata_by_doi():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    doi = dict.get('publications.doi')
    url = f"{base_api_uri}/v1/publications/doi?doi={doi}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of publication by doi: url {url}, headers {headers}")
    logging.info(f"Params: doi = {doi}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publications/id/{id}
def get_extended_metadata_by_id():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    publication_id = dict.get('publications.id')
    url = f"{base_api_uri}/v1/publications/id/{publication_id}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for extended metadata of publication by id: url {url}, headers {headers}")
    logging.info(f"Params: id = {publication_id}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publications/page
def get_page_by_status():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('publications.page')
    size = dict.get('publications.size')
    status = dict.get('publications.status')
    url = f"{base_api_uri}/v1/publications/page?page={page}&size={size}&status={status}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of publications: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}, status = {status}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/publications/version/{version}
def get_metadata_by_version():
    headers = TokenService.get_headers()
    base_api_uri = dict.get('base.api.uri')
    version = dict.get('publications.version')
    url = f"{base_api_uri}/v1/publications/version/{version}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for metadata of publication by version: url {url}, headers {headers}")
    logging.info(f"Params: version = {version}")
    return response.text


# Metoda służy do wykonania żądania POST na końcówkę /v1/publications. Argumentem metody jest ciąg znaków w formacie json,
# wprowadzony przez użytkownika na stronie aplikacji demo. Przykładowy json zwarty jest w pliku single-article.json,
# jednakże w zależności od środowiska, na którym będzie wykonana metoda, dane zawarte w tym pliku mogą wymagać modyfikacji,
# np. w zakresie identyfikatorów podanych obiektów.
def add_or_edit_single_publication(publication):
    headers = TokenService.get_headers_with_user_token()
    base_api_uri = dict.get('base.api.uri')
    url = f"{base_api_uri}/v1/publications"
    response = requests.post(url=url, headers=headers, json=publication)
    logging.info(f"Sending POST request to add or edit publication: url {url}, headers {headers}")
    return response.text


# Metoda służy do wykonania żądania POST na końcówkę /v1/publications/import. Argumentem metody jest ciąg znaków w formacie json,
# wprowadzony przez użytkownika na stronie aplikacji demo. Przykładowy json zwarty jest w pliku multiple-book-and-chapter.json,
# jednakże w zależności od środowiska, na którym będzie wykonana metoda, dane zawarte w tym pliku mogą wymagać modyfikacji,
# np. w zakresie identyfikatorów podanych obiektów.
def add_or_edit_multiple_publications(publications):
    headers = TokenService.get_headers_with_user_token()
    base_api_uri = dict.get('base.api.uri')
    url = f"{base_api_uri}/v1/publications/import"
    response = requests.post(url=url, headers=headers, json=publications)
    logging.info(f"Sending POST request to add or edit multiple publications: url {url}, headers {headers}")
    return response.text
