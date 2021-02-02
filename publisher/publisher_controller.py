from flask import Blueprint
from publisher import publisher_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy publishers-controller (wyłączenie żądania typu GET)
publisher = Blueprint('publisher', __name__)


@publisher.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return publisher_service.get_extended_metadata_by_id()


@publisher.route("/metadata-by-id")
def get_metadata_by_id():
    return publisher_service.get_metadata_by_id()


@publisher.route("/page-mnisw")
def get_page_mnisw():
    return publisher_service.get_page_mnisw()


@publisher.route("/page-mnisw-yearlist")
def get_page_mnisw_year_list():
    return publisher_service.get_page_mnisw_year_list()


@publisher.route("/page-by-status")
def get_page_by_status():
    return publisher_service.get_page_by_status()


@publisher.route("/metadata-by-version")
def get_metadata_by_version():
    return publisher_service.get_metadata_by_version()
