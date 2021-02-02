from flask import Blueprint, render_template, request, redirect

from get_token.token_service import TokenService
from variables import dict

get_token = Blueprint('get_token', __name__)

# Końcówka służy do dostarczenia danych na stronę aplikacji demo:
# – adresu do uzyskania tokena jednorazowego (Get token)
# - informacji, czy uzyskano token użytkownika (jeżeli tak, wyświetlane są elementy służące do wykonywania poszczególnych zapytań).
# Po użyciu linka „Pobierz token użytkownika” następuje przekierowanie na adres służący do uzyskania jednorazowego tokena "oneTimeTokenUrl".
# Wymagane jest, aby w tej samej przeglądarce użytkownik zalogowany był do aplikacji PBN. Z tego adresu nastąpi przekierowanie
# na adres zwrotny aplikacji użytkownika, podany przy rejestracji roli Menadżer aplikacji w PBN.
# Wartość baseAuthUrl podana jest w pliku variables.py pod kluczem base.auth.uri. Wartość tą trzeba dostosować,
# np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/auth
# Wartość applicationId podana jest w pliku variables.py pod kluczem application.id. Odpowiada ona identyfikatorowi
# aplikacji użytkownika, podanemu przy rejestracji roli Menadżer aplikacji w PBN (X-App-Id).
@get_token.route("/")
def start_page():
    return render_template('home.html',
                           oneTimeTokenUrl=dict.get('base.auth.uri') + '/pbn/api/registration/user/token/' + dict.get(
                               'application.id'),
                           hasToken=TokenService.has_token())

# Końcówka znajduje się pod adresem podanym przy rejestracji roli Menadżer aplikacji w PBN. Rolą końcówki jest pozyskanie
# tokenu użytkownika na podstawie jednorazowego kodu z adresu url (zapytanie, parametr „ott”) przekazanego do obsługi
# do serwisu klasy TokenService, w którym opisano dalsze kroki.
# Przykładowe zapytanie do końcówki to: "localhost:5000/one-time-token?ott=c69df69c-f1da-4404-b3ea-4031b7399c45"
@get_token.route("/one-time-token")
def one_time_token_callback():
    ott = request.args.get('ott')
    TokenService.get_user_token(ott)
    return redirect('/')
