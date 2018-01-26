//
// {{ classname }}
//
// Automatically generated using YAMLJSONModel.
// Do not edit!
//

#import "{{ classname }}.h"

@implementation {{ classname }}

+ (JSONKeyMapper *)keyMapper
{
    return [[JSONKeyMapper alloc] initWithModelToJSONDictionary:@{
{% for property_name, value in properties.items() -%}
{% if value['keymap'] is defined -%}
        @"{{ property_name }}": @"{{ value['keymap'] }}",
{% endif -%} 
{% endfor -%}
    }];
}

@end
