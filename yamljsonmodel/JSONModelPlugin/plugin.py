from jinja2 import Environment, PackageLoader

def is_leaf_dict(d):
    """Return true if a dictionary contains a dictionary as a value"""
    
    for v in d.values():
        if type(v) == dict:
            return False
        
    return True

def foreach_prop(props, cb, parents = []):
    """Iterate over each property in a hash.  Execute callback containing
       parent property list, property and values. Handle """

    for key, value in props.items():
        if is_leaf_dict(value):
            cb(key, value, parents)
        else:
            foreach_prop(value, cb, parents + [key])
        
def make_template_vars(obj):

    # Drop out early if no properties
    
    if not obj.has_key('properties'):
        return {}

    props = obj['properties']

    # First pass - string values are shortcut names for types

    for key, value in props.items():
        if type(value) == str:
            props[key] = {'type': value}

    # Create template variables from properties

    vars = {}
    
    def fn(key, value, parents):

        vars[key] = {}
        
        vars[key]['protocols'] = []
        vars[key]['type'] = value['type']

        if value.has_key('collectionType'):
            vars[key]['collectionType'] = value['collectionType']

        if value.has_key('optional'):
            vars[key]['protocols'].append('Optional')
        
        if len(parents) > 0:
            vars[key]['keymap'] = '.'.join(parents) + '.' + key

    foreach_prop(props, fn)

    return vars

def process_yaml_object(kind, obj):
    """Generate JSONModel output from templates."""

    # Create template environment
    
    env = Environment(
        loader = PackageLoader('yamljsonmodel.JSONModelPlugin', 'templates')
    )

    # Generate model.h

    template = env.get_template('model.h')

    template_vars = {}
    template_vars['properties'] = make_template_vars(obj)
    template_vars['classname'] = obj['name']
    
    yield 'model.h', template.render(**template_vars)
