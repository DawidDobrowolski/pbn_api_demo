import logging

from flask import Flask

from authorprofile.author_profile_controller import author_profile
from conference.conference_controller import conference
from dictionary.dictionary_controller import dictionary
from home.home_controller import get_token
from institution.institution_controller import institution
from institution_profile.institution_profile_controller import institution_profile
from journal.journal_controller import journal
from person.person_controller import person
from publication.publication_controller import publication
from publisher.publisher_controller import publisher

app = Flask(__name__)
app.register_blueprint(get_token)
app.register_blueprint(author_profile, url_prefix='/author-profile')
app.register_blueprint(conference, url_prefix='/conferences')
app.register_blueprint(dictionary, url_prefix='/dictionary')
app.register_blueprint(institution, url_prefix='/institution')
app.register_blueprint(institution_profile, url_prefix='/institution-profile')
app.register_blueprint(journal, url_prefix='/journals')
app.register_blueprint(person, url_prefix='/person')
app.register_blueprint(publication, url_prefix='/publications')
app.register_blueprint(publisher, url_prefix='/publishers')

def logging_setup():
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    logging.getLogger().setLevel(logging.INFO)

if __name__ == "__main__":
    logging_setup()
    app.run()
