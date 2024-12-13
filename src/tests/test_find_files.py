################################################################
#
#    test_find_files.py
#
################################################################

import os
from pathlib import Path
from unittest import TestCase
from pronouns2 import *

class TestFindFiles(TestCase):
    def test_find_files_md(self):
        """Test find_files with '.md' pattern"""
        files = find_files(".", "*.md")
        self.assertEqual(len(files), 1)
        self.assertTrue(any(f.endswith("README.md") for f in files))
    
    def test_find_files_notebook(self):
        """Test find_files with Jupyter notebook pattern"""
        files = find_files(".", "*.ipynb")
        self.assertEqual(len(files), 1)
        self.assertTrue(any(f.endswith("spread.ipynb") for f in files))
    
    def test_find_files_makefile(self):
        """Test find_files with exact Makefile pattern"""
        files = find_files(".", "Makefile")
        self.assertEqual(len(files), 1)
    
    def test_find_files_python(self):
        """Test find_files with Python file pattern"""
        files = find_files(".", "*.py")
        self.assertGreater(len(files), 1)
    
    def test_find_files_table(self):
        """Test find_files with table-related patterns"""
        files = find_files(".", "table_*.py")
        self.assertEqual(len(files), 2)  # table_interp.py and table_proc.py
    
    def test_find_files_utility(self):
        """Test find_files with utility file patterns"""
        files = find_files(".", "*_uty.py")
        self.assertEqual(len(files), 2)  # primary_uty.py and secondary_uty.py
    
    def test_find_files_multi_extension(self):
        """Test find_files with multiple extension pattern"""
        files = find_files(".", "spread.*")
        self.assertEqual(len(files), 2)  # spread.py and spread.ipynb
    
    def test_find_files_single_char(self):
        """Test find_files with single character wildcard"""
        files = find_files(".", "te?.py")
        self.assertEqual(len(files), 1)  # tex.py
    
    def test_find_files_char_set(self):
        """Test find_files with character set pattern"""
        files = find_files(".", "[adv]*.py")  # files starting with a, d, or v
        self.assertGreater(len(files), 0)
        self.assertTrue(any(f.endswith("abstract.py") for f in files))
        self.assertTrue(any(f.endswith("doc.py") for f in files))
        self.assertTrue(any(f.endswith("view.py") for f in files))
    
    def test_find_files_proc(self):
        """Test find_files with processor file patterns"""
        files = find_files(".", "*_proc.py")
        self.assertEqual(len(files), 3)  # node_proc.py and table_proc.py
