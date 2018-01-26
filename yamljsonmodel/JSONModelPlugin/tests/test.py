import yamljsonmodel
import unittest

import yaml

class TestJSONModelPlugin(unittest.TestCase):

    def testClassname(self):
        """Test JSONModel classname"""

        doc = '''
---
- kind: JSONModel
  name: test
'''
        y = yaml.load(doc)

        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h': 
                self.assertIn("@interface test : JSONModel", template_value)
        
    def testProperties(self):
        """Test JSONModel properties"""
        
        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: 
      type: NSInteger
'''
        y = yaml.load(doc)
    
        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h':
                self.assertIn("NSInteger foo", template_value)            

    def testOptionalProperties(self):
        """Test JSONModel optional properties"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: 
      type: NSInteger
    bar: 
      type: NSInteger
      optional: true
'''
        y = yaml.load(doc)

        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h':
                self.assertIn("NSInteger <Optional> bar", template_value)

    def testOnlyOptionalProperties(self):
        """Test JSONModel with only optional properties"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: 
      type: NSInteger
      optional: true
'''

        y = yaml.load(doc)

        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h':
                self.assertIn("NSInteger <Optional> foo", template_value)

    def testNestedProperties(self):
        """Test JSONModel nested properties behind a keymap"""
        
        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    auth:
      identity:
        username: 
          type: NSString *
'''
        y = yaml.load(doc)

        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h':
                self.assertIn("NSString * username", template_value)
                self.assertIn("keymap = auth.identity.username", template_value)

    def testTypeShortcut(self):
        """Test JSONModel shortcut for simple property"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: NSString *
'''
        y = yaml.load(doc)

        for template_name, template_value in yamljsonmodel.process_yaml_document(y):
            if template_name == 'model.h':
                self.assertIn("NSString * foo", template_value)
