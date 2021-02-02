from flask import Blueprint
from institution import institution_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy institution-controller (wyłączenie żądania typu GET)

institution = Blueprint('institution', __name__)


@institution.route("/page-by-status")
def get_page_by_status():
    return institution_service.get_page_by_status()


@institution.route("/page-polon")
def get_page_polon():
    return institution_service.get_page_polon()


@institution.route("/metadata-by-polon-uid")
def get_metadata_by_polon_uid():
    return institution_service.get_metadata_by_polon_uid()


@institution.route("/metadata-by-polon-id")
def get_metadata_by_polon_id():
    return institution_service.get_metadata_by_polon_id()


@institution.route("/metadata-by-version")
def get_metadata_by_version():
    return institution_service.get_metadata_by_version()


@institution.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return institution_service.get_extended_metadata_by_id()


@institution.route("/metadata-by-id")
def get_metadata_by_id():
    return institution_service.get_metadata_by_id()
