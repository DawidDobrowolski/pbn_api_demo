from flask import Blueprint
from person import person_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy person-controller (wyłączenie żądania typu GET)
person = Blueprint('person', __name__)


@person.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return person_service.get_extended_metadata_by_id()

@person.route("/employees-by-institution-id")
def get_employees_by_institution_id():
    return person_service.get_employees_by_institution_id()

@person.route("/metadata-by-natural-id")
def get_metadata_natural_by_id():
    return person_service.get_metadata_natural_by_id()

@person.route("/page-by-status")
def get_page_by_status():
    return person_service.get_page_by_status()

@person.route("/metadata-by-polon-uid")
def get_metadata_by_polon_uid():
    return person_service.get_metadata_by_polon_uid()

@person.route("/metadata-by-version")
def get_metadata_by_version():
    return person_service.get_metadata_by_version()