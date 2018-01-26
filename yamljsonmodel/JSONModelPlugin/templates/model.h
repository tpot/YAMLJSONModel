//
// {{ classname }}
//
// Automatically generated using YAMLJSONModel.
// Do not edit!
//

@interface {{ classname }} : JSONModel

{% if properties is defined -%}
{% for property_name, value in properties.items() -%}
@property (nonatomic) {{ value['type'] }} {% if value['protocols']|length > 0 %}<{{value['protocols']|join(',')}}> {% endif %}{{ property_name }};{% if value['keymap'] is defined %}            // keymap = {{ value['keymap'] }}{% endif %}
{% endfor -%}
{% endif %}
@end
