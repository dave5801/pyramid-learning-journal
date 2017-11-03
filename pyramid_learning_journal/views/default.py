# views.py
# ...
#from pyramid.renderers import render --> likely do this here.
#import a data/data.py file - which will hold iterable data to be injected into html templates
from pyramid.view import view_config
import io
import os
from pyramid.response import Response

''''
list_view: for the list of journal entries
detail_view: for a single journal entry
create_view: for creating a new view
update_view: for updating an existing view
'''



ENTRIES = [
    {
    'title': 'Entry 1',
    'body': 'Text Goes Here',
    'date': 'xxxx-xx-xx'
    },
    {
    'title': 'Entry 2',
    'body': 'Text Goes Here',
    'date': 'xxxx-xx-xx'
    }
]


@view_config(route_name='list_view', renderer='../templates/index.jinja2')
def list_view(request):
    return {'entries': ENTRIES} # <--- notice, it returns an empty dictionary

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