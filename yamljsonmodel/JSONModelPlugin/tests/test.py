import yamljsonmodel
import unittest

import yaml

class TestJSONModelPlugin(unittest.TestCase):

    def testProperties(self):
        """Test JSONModel properties"""
        
        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: NSInteger
'''

        y = yaml.load(doc)
    
        def foo(s):
            self.assertIn("NSInteger foo", s)
    
        yamljsonmodel.process_yaml_document(y, lambda x: foo(x))

    def testOptionalProperties(self):
        """Test JSONModel optional properties"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: NSInteger
  optional_properties:
    bar: NSInteger
'''
        y = yaml.load(doc)

        def foo(s):
            self.assertIn("NSInteger <Optional> bar", s)

        yamljsonmodel.process_yaml_document(y, lambda x: foo(x))

    def testOnlyOptionalProperties(self):
        """Test JSONModel with only optional properties"""

        doc = '''
---
- kind: JSONModel
  name: test
  optional_properties:
    foo: NSInteger
'''

        y = yaml.load(doc)

        def foo(s):
            self.assertIn("NSInteger <Optional> foo", s)

        yamljsonmodel.process_yaml_document(y, lambda x: foo(x))
