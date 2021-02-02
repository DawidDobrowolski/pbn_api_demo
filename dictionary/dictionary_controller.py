from flask import Blueprint
from dictionary import dictionary_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy dictionary-controller (wyłączenie żądania typu GET)

dictionary = Blueprint('dictionary', __name__)


@dictionary.route("/countries")
def get_countries():
    return dictionary_service.get_countries()


@dictionary.route("/disciplines")
def get_disciplines():
    return dictionary_service.get_disciplines()


@dictionary.route("/languages")
def get_languages():
    return dictionary_service.get_languages()
