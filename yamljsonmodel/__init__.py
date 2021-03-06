import pkg_resources

# Load plugins using pkg_resources

plugins = {
    entry_point.name: entry_point.load()
    for entry_point in pkg_resources.iter_entry_points('yamljsonmodel.plugins')
}

def process_yaml_document(yamldoc):

    for obj in yamldoc:

        kind = obj['kind']

        if not plugins.has_key(kind):
            raise Exception('No plugin named %s' % kind)

        plugin = plugins[kind]

        return plugin.process_yaml_object(obj)
