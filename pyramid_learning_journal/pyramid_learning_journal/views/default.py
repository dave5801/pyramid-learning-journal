# views.py
# ...
import io
import os
from pyramid.response import Response

''''
list_view: for the list of journal entries
detail_view: for a single journal entry
create_view: for creating a new view
update_view: for updating an existing view
'''

HERE = os.path.dirname(__file__)

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