from flask import Blueprint
from conference import conference_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy conferences-controller (wyłączenie żądania typu GET)
conference = Blueprint('conference', __name__)


@conference.route("/page-mnisw")
def get_page_mnisw():
    return conference_service.get_page_mnisw()


@conference.route("/page-by-status")
def get_page_by_status():
    return conference_service.get_page_by_status()


@conference.route("/metadata-by-version")
def get_metadata_by_version():
    return conference_service.get_metadata_by_version()


@conference.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return conference_service.get_extended_metadata_by_id()


@conference.route("/editions")
def get_editions():
    return conference_service.get_editions()


@conference.route("/metadata-by-id")
def get_metadata_by_id():
    return conference_service.get_metadata_by_id()
