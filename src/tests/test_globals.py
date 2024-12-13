################################################################
#
#    test_globals.py
#
################################################################

import io
import sys
from enum import Enum, IntEnum
from typing import Optional
from unittest import TestCase
from pronouns2 import *

class TestGlobals(TestCase):
    def test_globals_FeatureIndex_repr(self):
        """Test 'class FeatureIndex(Enum)' 'def __repr__(self)' """
        self.assertEqual(f"{FeatureIndex.PNF}", "FeatureIndex.PNF")
        self.assertEqual(f"{FeatureIndex.FPF}", "FeatureIndex.FPF")
        self.assertEqual(f"{FeatureIndex.SPF}", "FeatureIndex.SPF")
        self.assertEqual(f"{FeatureIndex.TPF}", "FeatureIndex.TPF")
        self.assertEqual(f"{FeatureIndex.PLF}", "FeatureIndex.PLF")
        self.assertEqual(f"{FeatureIndex.GNF}", "FeatureIndex.GNF")
        self.assertEqual(f"{FeatureIndex.ANF}", "FeatureIndex.ANF")
        self.assertEqual(f"{FeatureIndex.RPF}", "FeatureIndex.RPF")
        self.assertEqual(f"{FeatureIndex.GEN}", "FeatureIndex.GEN")
    def test_globals_NodeId_repr(self):
        """Test 'class NodeId(Enum)' 'def __repr__(self)' """
        self.assertEqual(f"{NodeId.C_NODE}", "NodeId.C_NODE")
        self.assertEqual(f"{NodeId.S_NODE}", "NodeId.S_NODE")
        self.assertEqual(f"{NodeId.N_NODE}", "NodeId.N_NODE")
        self.assertEqual(f"{NodeId.E_NODE}", "NodeId.E_NODE")
    def test_globals_Feature_repr(self):
        """Test 'class Feature(Enum)' 'def __repr__(self)' """
        self.assertEqual(f"{Feature.PLUS}", "Feature.PLUS")
        self.assertEqual(f"{Feature.MINUS}", "Feature.MINUS")
        self.assertEqual(f"{Feature.QUESTION}", "Feature.QUESTION")
    def test_globals_FileType_repr(self):
        """Test 'class FileType' 'def __repr__(self)' """
        self.assertEqual(f"{FileType.TXT}", "FileType.TXT")
        self.assertEqual(f"{FileType.TEX}", "FileType.TEX")
    def test_globals_FileType_file_ext(self):
        """Test 'class FileType' 'def file_ext(self)' """
        self.assertEqual(FileType.TXT.file_ext, ".txt")
        self.assertEqual(FileType.TEX.file_ext, ".tex")
    def test_globals_FileType_from_ext(self):
        """Test 'class FileType' 'def from_ext(ext: str)' """
        self.assertEqual(FileType.from_ext(".txt"), FileType.TXT)
        self.assertEqual(FileType.from_ext(".tex"), FileType.TEX)
    def test_globals_Node_tree(self):
        """Test 'class Node' 'def set_tree(cls, new_tree)' and 'def tree(cls)' """
        node = Node()
        node.number = 123
        node.lit = "Abc"
        node.sub = "x"
        Node.set_tree(node)
        self.assertEqual(Node.tree().number, 123)
        self.assertEqual(Node.tree().lit, "Abc")
        self.assertEqual(Node.tree().sub, "x")
    def test_globals_Summary(self):
        """Test 'class Summary' """
        Summary.meaningless = 37
        Summary.meaningful = 60
        Summary.ambiguous = 15
        Summary.correct = 77
        Summary.total = 110
        self.assertEqual(Summary.meaningless, 37)
        self.assertEqual(Summary.meaningful, 60)
        self.assertEqual(Summary.ambiguous, 15)
        self.assertEqual(Summary.correct, 77)
        self.assertEqual(Summary.total, 110)
    def test_globals_Manager(self):
        """Test 'class Manager' """
        self.assertTrue(isinstance(Manager.state, dict))
        self.assertTrue(isinstance(Manager.manager, Manager))
        info = Manager.info
        debug = Manager.debug
        trace = Manager.trace
        chaining_diagram = Manager.chaining_diagram
        self.assertTrue(isinstance(info, bool))
        self.assertTrue(isinstance(debug, bool))
        self.assertTrue(isinstance(trace, bool))
        self.assertTrue(isinstance(chaining_diagram, bool))
        self.assertEqual(info, Manager.state['info'])
        self.assertEqual(debug, Manager.state['debug'])
        self.assertEqual(trace, Manager.state['trace'])
        self.assertEqual(chaining_diagram, Manager.state['chaining_diagram'])
        with Manager.manager:
            Manager.set_state(info=(not info),
                              debug=(not debug),
                              trace=(not trace),
                              chaining_diagram=(not chaining_diagram))
            self.assertEqual(Manager.info, not info)
            self.assertEqual(Manager.debug, not debug)
            self.assertEqual(Manager.trace, not trace)
            self.assertEqual(Manager.chaining_diagram, not chaining_diagram)
        self.assertEqual(Manager.info, info)
        self.assertEqual(Manager.debug, debug)
        self.assertEqual(Manager.trace, trace)
        self.assertEqual(Manager.chaining_diagram, chaining_diagram)
        self.assertTrue(isinstance(Manager.stream, io.TextIOBase))
        self.assertTrue(isinstance(Manager.file_type, FileType))

