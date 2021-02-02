from flask import Blueprint
from authorprofile import author_profile_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy author-profile-controller (wyłączenie żądania typu GET)

author_profile = Blueprint('author_profile', __name__)


@author_profile.route("/profile-by-id")
def get_profile_by_id():
    return author_profile_service.get_profile_by_id()
