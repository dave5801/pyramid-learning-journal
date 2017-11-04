"""View routes."""
from .default import list_view
from .default import single_page_view
from .default import new_entry_view
from .default import edit_view


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(list_view, route_name='list_view')
    config.add_view(single_page_view, route_name='single_page_view')
    config.add_view(new_entry_view, route_name='new_entry_view')
    config.add_view(edit_view, route_name='edit_view')
