from flask import Blueprint
from journal import journal_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy journals-controller (wyłączenie żądania typu GET)
journal = Blueprint('journal', __name__)


@journal.route("/page-mnisw")
def get_page_mnisw():
    return journal_service.get_page_mnisw()


@journal.route("/page-by-status")
def get_page_by_status():
    return journal_service.get_page_by_status()


@journal.route("/metadata-by-version")
def get_metadata_by_version():
    return journal_service.get_metadata_by_version()


@journal.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return journal_service.get_extended_metadata_by_id()


@journal.route("/metadata-by-id")
def get_metadata_by_id():
    return journal_service.get_metadata_by_id()
