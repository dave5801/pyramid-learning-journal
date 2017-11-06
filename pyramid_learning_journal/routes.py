def includeme(config):
    """Include the following routes for static files and uri paths."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('single_page_view', '/single_page_view')
    config.add_route('new_entry_view', '/new_entry_view')
    config.add_route('edit_view', '/edit_view')

#learning_journal/journal/5