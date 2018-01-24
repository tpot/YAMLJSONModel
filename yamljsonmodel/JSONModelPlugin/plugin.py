from jinja2 import Environment, PackageLoader

def add_keymaps_for_properties(keypath, properties):
    result = {}
    for key in properties.keys():
        if type(properties[key]) == dict:
            result.update(add_keymaps_for_properties(keypath + [key], properties[key]))
        else:
            result[key] = {"type": properties[key],
                           "keymap": ".".join(keypath + [key])}
            
    return result
        
def make_template_vars(obj):

    vars = {}
    vars['classname'] = obj['name']
    vars['properties'] = {}

    # Required properties

    for key in ['properties', 'optional_properties']:

        if obj.has_key(key):

            for name in obj[key].keys():

                # String value is shortcut for simple property
                
                if type(obj[key][name]) == str:
                    vars['properties'][name] = {'type': obj[key][name]}

                # Hash value is nested properties

                if type(obj[key][name]) == dict:
                    nested = add_keymaps_for_properties([name], obj[key][name])
                    vars['properties'].update(nested)
                    
                # Mark as optional
                
                if key == 'optional_properties':
                    vars['properties'][name]['protocols'] = ['Optional']

    return vars        

def process_yaml_object(kind, obj):
    """Generate JSONModel output from templates."""

    # Create template environment
    
    env = Environment(
        loader = PackageLoader('yamljsonmodel.JSONModelPlugin', 'templates')
    )

    # Generate model.h

    template = env.get_template('model.h')

    template_vars = make_template_vars(obj)
    return template.render(**template_vars)
