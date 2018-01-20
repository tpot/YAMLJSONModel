//
// {{ name }}.h
//
// Automatically generated using YAMLJSONModel.
// Do not edit!
//

@interface {{ name }} : JSONModel

// Required properties

{% for name, type in properties.items() -%}
@property (nonatomic) {{ type }} {{ name }};
{% endfor %}
@end
