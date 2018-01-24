//
// {{ classname }}
//
// Automatically generated using YAMLJSONModel.
// Do not edit!
//

@interface {{ classname }} : JSONModel

// Required properties

{% if properties is defined -%}
{% for property_name, value in properties.items() -%}
@property (nonatomic) {{ value['type'] }} {{ property_name }};
{% endfor -%}
{% endif %}
// Optional properties

{% if optional_properties is defined -%}
{% for property_name, value in optional_properties.items() -%}
@property (nonatomic) {{ value['type'] }} <{{value['protocols']|join(',')}}> {{ property_name }};
{% endfor -%}
{% endif %}
@end
