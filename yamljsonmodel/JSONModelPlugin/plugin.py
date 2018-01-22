from jinja2 import Environment, PackageLoader

def map_variables(variables):
    
    mapped_variables = {}
    
    for key, value in variables.items():

        # Expand scalar value to a hash

        if type(value) == str:
            mapped_variables[key] = {"type": value}
        else:
            mapped_variables[key] = value
            
    return mapped_variables

def process_yaml_object(kind, obj):
    """Generate JSONModel output from templates."""

    # Create template environment
    
    env = Environment(
        loader = PackageLoader('yamljsonmodel', 'templates')
    )

    # Generate model.h

    template = env.get_template('%s/model.h' % kind)

    mapped_variables = obj.copy()
    for key in ['properties', 'optional_properties']:
        if mapped_variables.has_key(key):
            mapped_variables[key] = map_variables(obj[key])

    return template.render(**mapped_variables)
