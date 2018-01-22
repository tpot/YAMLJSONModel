//
// {{ name }}.h
//
// Automatically generated using YAMLJSONModel.
// Do not edit!
//

@interface {{ name }} : JSONModel

// Required properties

{% if properties is defined -%}
{% for property_name, values in properties.items() -%}
@property (nonatomic) {{ values['type'] }} {{ property_name }};
{% endfor -%}
{% endif %}
// Optional properties

{% if optional_properties is defined -%}
{% for property_name, values in optional_properties.items() -%}
@property (nonatomic) {{ values['type'] }} <Optional> {{ property_name }};
{% endfor -%}
{% endif %}
@end
