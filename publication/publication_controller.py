from flask import Blueprint, request
from publication import publication_service

# Niniejszy kontroler służy do obsługi żądań z niniejszej aplikacji demo. Przekazuje żądanie do serwisu, który zajmuje się
# komunikacją z API PBN, a odpowiedź uzyskaną z serwisu przekazuje do wyświetlenia na stronie aplikacji demo.
# Kontroler pośredniczy przy obsłudze API PBN z grupy publications-controller (żądania typu GET i POST).
# W przypadku, gdy wynikiem żądania POST jest odpowiedź o statusie http 400 "Bad Request", co najprawdopodobniej oznacza,
# że wysłany json nie przeszedł walidacji - odpowiedź uzyskana z API PBN jest przekształcana w taki sposób,
# aby ciało tej odpowiedzi było odebrane przez przeglądarkę i wyświetlone na stronie aplikacji demo.
# Konieczność takiego przekształcenia jest spowodowana specyfiką używanego frameworka.
publication = Blueprint('publication', __name__)


@publication.route("/metadata-by-id")
def get_metadata_by_id():
    return publication_service.get_metadata_by_id()


@publication.route("/metadata-by-doi")
def get_metadata_by_doi():
    return publication_service.get_metadata_by_doi()


@publication.route("/extended-metadata-by-id")
def get_extended_metadata_by_id():
    return publication_service.get_extended_metadata_by_id()


@publication.route("/page-by-status")
def get_page_by_status():
    return publication_service.get_page_by_status()


@publication.route("/metadata-by-version")
def get_metadata_by_version():
    return publication_service.get_metadata_by_version()


@publication.route("/add-or-edit-single-publication", methods=['POST'])
def add_or_edit_single_publication():
    publication_data = request.json
    return publication_service.add_or_edit_single_publication(publication_data)


@publication.route("/add-or-edit-multiple-publications", methods=['POST'])
def add_or_edit_multiple_publications():
    publications_data = request.json
    return publication_service.add_or_edit_multiple_publications(publications_data)
