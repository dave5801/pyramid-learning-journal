"""Views."""

from pyramid.view import view_config
import os

ENTRIES = [
    {'title': 'Entry 1', 'body': 'Fought Ninjas', 'date': '11-SMarch-17'},
    {'title': 'Entry 2', 'body': 'Awesome Stuff', 'date': '12-SMarch-17'},
    {'title': 'Entry 3', 'body': 'Spiders!', 'date': '13-SMarch-17'},
]


@view_config(route_name='list_view', renderer='../templates/journal_entries.jinja2')
def list_view(request):
    """Display Journal Entries."""
    return {'entries': ENTRIES}


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


#use {%block content%}To build blocks of html content {%end block%} --> may avoid repetition of html

##Likely return data structures to be rendered in templates here.

#html that goes on every page goes on layout.jinja2
# new html goes into file_name.jinja2 {% extends "layout.jinja2" %}

HERE = os.path.dirname(__file__)

''''
def list_view(request):
    """Serve all journal entries on home page."""
    with io.open(os.path.join(HERE, '../templates/index.html')) as file:
        imported_html = file.read()
    return Response(imported_html)

def detail_view(request):
    """Serve details of single page."""
    with io.open(os.path.join(HERE, '../templates/single_page.html')) as file:
        imported_html = file.read()
    return Response(imported_html)

def create_view(request):
    """Serve create new page."""
    with io.open(os.path.join(HERE, '../templates/new_entry.html')) as file:
        imported_html = file.read()
    return Response(imported_html)

def update_view(request):
    """Serve edit entry page."""
    with io.open(os.path.join(HERE, '../templates/edit.html')) as file:
        imported_html = file.read()
    return Response(imported_html)
# ...
'''