import logging
import requests
from get_token.token_service import TokenService
from variables import dict


# Serwis zawiera metody wykonujące żądania REST do poszczególnych końcówek API PBN z grupy institution-profile-controller (wyłączenie żądania typu GET).
# We wszystkich przypadkach typu:  ... = dict.get("..."), tworzona jest zmienna o nazwie zgodnej z nazwą parametru ścieżki
# lub parameteru zapytania, podanymi w dokumentacji API PBN, przy czym argumentem jest klucz z pliku variables.py, a zmienna uzyskuje wartość
# zgodną z wartością przypisaną do tego klucza w tym pliku. Tak utworzone zmienne wykorzystywane są do utworzenia właściwego adresu URL, zgodnego
# z dokumentacją API PBN. Przy utworzeniu adresu wykorzystywana jest także zmienna base_api_uri, której wartość podana jest w pliku variables.py
# pod kluczem base.api.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
# Do każdego żądania dodawane są nagłówki, pobierane z serwisu klasy TokenService za pomocą metody get_headers_with_user_token, przy której podane szczegółowe informacje o tych nagłówkach.
# W każdym przypadku odpowiedż z końcówki API PBN przykazywana jest do właściwego kontrolera i wyświetlana na stronie aplikacji demo.

# Metoda służy do wykonania żądania GET na końcówkę /v1/institutionProfile/publications/page
def get_publications_page():
    headers = TokenService.get_headers_with_user_token()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('institution.profile.page')
    size = dict.get('institution.profile.size')
    url = f"{base_api_uri}/v1/institutionProfile/publications/page?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(
        f"Sending GET request for page of publications from institution's profile: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text


# Metoda służy do wykonania żądania GET na końcówkę /v1/institutionProfile/publications/page/statements
def get_statements_page():
    headers = TokenService.get_headers_with_user_token()
    base_api_uri = dict.get('base.api.uri')
    page = dict.get('institution.profile.page')
    size = dict.get('institution.profile.size')
    url = f"{base_api_uri}/v1/institutionProfile/publications/page/statements?page={page}&size={size}"
    response = requests.get(url=url, headers=headers)
    logging.info(f"Sending GET request for page of statements from institution's profile: url {url}, headers {headers}")
    logging.info(f"Query params: page = {page}, size = {size}")
    return response.text
