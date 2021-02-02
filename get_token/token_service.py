import requests
from variables import dict


class TokenService:
    userToken: str = None

    # Metoda służy do uzyskania tokena użytkownika za pomocą uzyskanego wcześniej tokena jednorazowego. W tym celu wysyłane jest żądanie POST z nagłówkami:
    # (1) o nazwie „X-App-Id” i wartości zmiennej applicationId
    # (2) o nazwie „X-App-Token” i wartości zmiennej applicationToken,
    # a także ciałem typu json o wartości: {"oneTimeToken": oneTimeToken}, gdzie zmienna oneTimeToken oznacza uzyskany wcześniej token jednorazowy.
    # Wartość applicationId (X-App-Id) podana jest w pliku variables.py pod kluczem application.id. Odpowiada ona identyfikatorowi aplikacji użytkownika, podanemu przy rejestracji roli Menadżer aplikacji w PBN.
    # Wartość applicationToken (X-App-Token) podana jest w pliku variables.py pod kluczem application.token. Odpowiada ona tokenowi aplikacji użytkownika, uzyskanemu przy rejestracji roli Menadżer aplikacji w PBN.
    # Wartość baseAuthUrl podana jest w pliku variables.py pod kluczem base.auth.uri. Wartość tą trzeba dostosować, np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/auth
    # Odpowiedź na żądanie zawiera ciało typu json, w którym pod kluczem X-User-Token zawarty jest token użytkownika. Zostaje on zapisany joko pole niniejszego serwisu, w celu późniejszego wykorzystania.
    # W przypadku wystąpienia błędu proszę o sprawdzenie poprawności parametrów w pliku application.properties (application.id, application.token, base.auth.uri).
    def get_user_token(one_time_token):
        headers = {'X-App-Id': dict.get('application.id'),
                   'X-App-Token': dict.get('application.token')}
        body = {"oneTimeToken": one_time_token}
        url = dict.get('base.auth.uri') + '/pbn/api/user/token'
        response = requests.post(url=url, json=body, headers=headers)
        TokenService.userToken = response.json()['X-User-Token']

    @staticmethod
    def has_token():
        return TokenService.userToken != None

    # Metoda dostarcza innym serwisom obiekt reprezentujący nagłówki dodawane do każdego żądania wysyłanego do API PBN.
    # Nagłówki są następujące:
    # (1) o nazwie „X-App-Id” i wartości zmiennej applicationId
    # (2) o nazwie „X-App-Token” i wartości zmiennej applicationToken,
    # Wartość applicationId (X-App-Id) podana jest w pliku variables.py pod kluczem application.id. Odpowiada ona identyfikatorowi aplikacji użytkownika, podanemu przy rejestracji roli Menadżer aplikacji w PBN.
    # Wartość applicationToken (X-App-Token) podana jest w pliku variables.py pod kluczem application.token. Odpowiada ona tokenowi aplikacji użytkownika, uzyskanemu w wyniku rejestracji roli Menadżer aplikacji w PBN.
    @staticmethod
    def get_headers():
        headers = {'X-App-Id': dict.get('application.id'),
                   'X-App-Token': dict.get('application.token')}
        return headers

    # Metoda dostarcza innym serwisom obiekt reprezentujący nagłówki dodawane do każdego żądania wysyłanego do API PBN, które wymaga dodatkowo X-User-Token.
    # Nagłówki są następujące:
    # (1) o nazwie „X-App-Id” i wartości zmiennej applicationId
    # (2) o nazwie „X-App-Token” i wartości zmiennej applicationToken,
    # (2) o nazwie „X-User-Token” i wartości zmiennej userToken.
    # Wartość applicationId (X-App-Id) podana jest w pliku variables.py pod kluczem application.id. Odpowiada ona identyfikatorowi aplikacji użytkownika, podanemu przy rejestracji roli Menadżer aplikacji w PBN.
    # Wartość applicationToken (X-App-Token) podana jest w pliku variables.py pod kluczem application.token. Odpowiada ona tokenowi aplikacji użytkownika, uzyskanemu w wyniku rejestracji roli Menadżer aplikacji w PBN.
    # Wartość userToken (X-User-Token) została uzyskana za pomocą metody get_user_token (powyżej), a następnie zapisana jako pole niniejszego serwisu.
    @staticmethod
    def get_headers_with_user_token():
        headers = TokenService.get_headers()
        headers['X-User-Token'] = TokenService.userToken
        return headers
