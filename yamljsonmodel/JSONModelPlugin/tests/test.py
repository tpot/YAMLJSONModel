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
        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h': 
                self.assertIn("@interface test : JSONModel", tvalue)
        
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
        ydoc = yaml.load(doc)
    
        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("NSInteger foo", tvalue)            

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
        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("NSInteger <Optional> bar", tvalue)

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

        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("NSInteger <Optional> foo", tvalue)

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
        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("NSString * username", tvalue)
                self.assertIn("keymap = auth.identity.username", tvalue)

    def testTypeShortcut(self):
        """Test JSONModel shortcut for simple property"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: NSString *
'''
        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("NSString * foo", tvalue)

    def testKeyMapper(self):
        """Test JSONModel keymapper"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo: 
      bar: 
        type: NSString *
'''

        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.c':
                self.assertIn('@"bar": @"foo.bar",', tvalue)

    def testCollectionType(self):
        """Test JSONMapper property with collection type"""

        doc = '''
---
- kind: JSONModel
  name: test
  properties:
    foo:
      type: NSArray *
      collectionType: NSString *
'''
        ydoc = yaml.load(doc)

        for tname, tvalue in yamljsonmodel.process_yaml_document(ydoc):
            if tname == 'model.h':
                self.assertIn("<NSString *>", tvalue)
        
