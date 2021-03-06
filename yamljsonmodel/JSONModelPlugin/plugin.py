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
            props[key] = {'_type': value}

    # Create template variables from properties

    vars = {}
    
    def fn(key, value, parents):

        keyname = key
        if value.has_key('_keyname'):
            keyname = value['_keyname']
        
        if vars.has_key(keyname):
            raise Exception("Duplicate key, '%s'" % keyname)

        vars[keyname] = {}
        
        vars[keyname]['protocols'] = []
        vars[keyname]['type'] = value['_type']

        if value.has_key('_collectionType'):
            vars[keyname]['collectionType'] = value['_collectionType']

        if value.has_key('_optional'):
            vars[keyname]['protocols'].append('Optional')

        if value.has_key('_collectionType'):
            vars[keyname]['protocols'].append(value['_collectionType'])

        # Create keymap
            
        keymap = []

        if len(parents) > 0:
            # Nested properties require a keymap
            keymap = parents + [key]
        elif keyname != key:
            # We have used _keyname at top level
            keymap = [key]
            
        if len(keymap) > 0:
            vars[keyname]['keymap'] = '.'.join(keymap)
            
    foreach_prop(props, fn)

    return vars

def process_yaml_object(obj):
    """Generate JSONModel output from templates."""

    # Create template environment
    
    env = Environment(
        loader = PackageLoader('yamljsonmodel.JSONModelPlugin', 'templates')
    )

    # Generate model templates

    for name in ['model.h', 'model.c']:
        
        template = env.get_template(name)

        template_vars = {}
        template_vars['properties'] = make_template_vars(obj)
        template_vars['classname'] = obj['name']
    
        yield name, template.render(**template_vars)
