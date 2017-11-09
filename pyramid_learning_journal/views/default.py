"""Views."""
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
import os
from pyramid_learning_journal.models import Entries


@view_config(route_name='list_view', renderer='../templates/journal_entries.jinja2')
def list_view(request):
    """Display Journal Entries."""
    entries = request.dbsession.query(Entries).all()
    return {
    'entries': entries,
    'route': 'list_view'
    }


@view_config(route_name='single_page_view', renderer='../templates/single_page.jinja2')
def single_page_view(request):
    """Display Single Page Entries."""
    return {}


@view_config(route_name='new_entry_view', renderer='../templates/new_entry_page.jinja2')
def new_entry_view(request):
    """Display New Page Entries."""
    return {}


@view_config(route_name='edit_view', renderer='../templates/edit_page.jinja2')
def edit_view(request):
    """Display Edit Page."""
    return {}


HERE = os.path.dirname(__file__)
