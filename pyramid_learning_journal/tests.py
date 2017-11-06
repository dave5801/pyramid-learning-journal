"""This is the test class."""

import unittest
import transaction
from pyramid import testing


def dummy_request(dbsession):
    """Test for Dummy Requests."""
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    """I don't know what this is for yet."""
    def setUp(self):
        """Or this."""
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from .models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        """I guess this initializes a db."""
        from .models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        """The reading was a little hazy."""
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


class TestMyViewSuccessCondition(BaseTest):
    """Test success conditions"""

    def setUp(self):
        """haven't figured this out yet."""
        super(TestMyViewSuccessCondition, self).setUp()
        self.init_database()

        from .models import MyModel

        model = MyModel(name='one', value=55)
        self.session.add(model)

    def test_passing__journal_entries_to_listview(self):
        """Test pass journal entries to list view."""
        from .views.default import list_view

        test_content = [{'title': 'Entry 1', 'body': 'Fought Ninjas', 'date': '11-SMarch-17'},
        {'title': 'Entry 2', 'body': 'Awesome Stuff', 'date': '12-SMarch-17'}, 
        {'title': 'Entry 3', 'body': 'Spiders!', 'date': '13-SMarch-17'}]

        info = list_view(dummy_request(self.session))

        for i in test_content:
            self.assertTrue(i in info['entries'])


class TestViewContents(BaseTest):
    """Test contents of each view - when I have any, which I don't really at this point."""

    def test_listview_contents(self):
        """Test Confirms dictionary passed to list view."""
        from pyramid_learning_journal.views.default import list_view
        info = list_view(dummy_request(self.session))
        self.assertIsNotNone(info)
