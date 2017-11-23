"""Views."""
import datetime
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import os
from pyramid_learning_journal.models import Entries


@view_config(route_name='list_view', renderer='../templates/journal_entries.jinja2')
def list_view(request):
    """Display Journal Entries."""
    entries = request.dbsession.query(Entries).all()
    return {
        'entries': entries,
        'route': 'list_view',
    }


@view_config(route_name='single_page_view', renderer='../templates/single_page.jinja2')
def single_page_view(request):
    """Display Single Page Entries."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entries).get(the_id)
    
    if entry:
        return {
            "id": entry.id,
            "title": entry.title,
            "body": entry.body,
            "creation_date": entry.creation_date
            }
    else:
        raise HTTPNotFound



@view_config(route_name='new_entry_view', renderer='../templates/new_entry_page.jinja2')
def new_entry_view(request):
    """Display New Page Entries."""
    if request.method == "POST" and request.POST:
        form_data = request.POST
        new_entry = Entries(
                title=form_data['title'],
                body=form_data['body'],
                creation_date=datetime.datetime.now()
            )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('list_view'))
    return {}
'''
'''
@view_config(route_name='edit_view', renderer='../templates/edit_page.jinja2')
def edit_view(request):
    """Display Edit Page."""

    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entries).get(entry_id)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return {
            'entry': entry.to_dict()
        }
    if request.method == "POST":
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        entry.creation_date = datetime.datetime.now()
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('list_view'))
    return {}


HERE = os.path.dirname(__file__)

