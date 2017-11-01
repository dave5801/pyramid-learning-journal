def includeme(config):
    """Include the following routes for static files and uri paths."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/detail_view')
    config.add_route('create_view', '/create_view')
    config.add_route('update_view', '/update_view')

#learning_journal/journal/5