"""This is the test class."""
import pytest
from pyramid import testing
import transaction
import datetime

from pyramid_learning_journal.models import (
    Entries,
    get_tm_session,
)

from pyramid_learning_journal.models.meta import Base

@pytest.fixture(scope="session")
def configuration(request):
    """Set up a Configurator instance.

    This Configurator instance sets up a pointer to the location of the
        database.
    It also includes the models from your app's model package.
    Finally it tears everything down, including the in-memory SQLite database.

    This configuration will persist for the entire duration of your PyTest run.
    """
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_database'
    })
    config.include("pyramid_learning_journal.models")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config

@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database.

    This uses the dbsession_factory on the configurator instance to create a
    new database session. It binds that session to the available engine
    and returns a new session for every call of the dummy_request object.
    """
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session

@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_dict(dummy_request):
    """List view returns Response Object."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)

@pytest.fixture()
def testapp():
    from pyramid_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Contact Info Goes here - in the footer' in html.find("footer").text

def test_root_contents(testapp):
    response = testapp.get('/', status=200)
    html = response.html
    assert 3 == len(html.findAll(class_="journal_entries"))

def test_model_gets_added(db_session):

    assert len(db_session.query(Entries).all()) == 0
    model = Entries(
        title="Fake Title",
        body="Some description text",
        creation_date=datetime.datetime.now(),
    )
    db_session.add(model)
    assert len(db_session.query(Entries).all()) == 1

def test_list_view_returns_count_matching_database(dummy_request):
    from pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entries']) == 0