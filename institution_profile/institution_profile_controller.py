from flask import Blueprint

from institution_profile import institution_profile_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy institution-profile-controller (wyłączenie żądania typu GET)

institution_profile = Blueprint('institution_profile', __name__)


@institution_profile.route("/publications-page")
def get_publications_page():
    return institution_profile_service.get_publications_page()


@institution_profile.route("/statements-page")
def get_statements_page():
    return institution_profile_service.get_statements_page()
