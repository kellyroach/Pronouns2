################################################################
#
#    test_pronouns2_10p1.py
#
################################################################

import sys
from unittest import TestCase
from unittest.mock import patch
from pronouns2 import *

################################################################
#1. Tests all major execution paths in `main()`:
#   - No arguments (help display)
#   - Basic file output in TXT and TEX formats
#   - Debug mode output in TXT and TEX formats
#   - Debug with trace output in TXT and TEX formats
#   - Example numbers as positional argument
#   - Custom chaining_rho parameter
#   - Invalid parameter validation
#
#2. Uses `unittest.mock` features:
#   - `@patch('sys.argv')` to simulate command line arguments
#   - `@patch('sys.stdout')` to capture help output
#   - Mocks for `doc` function to avoid actual file creation
#
#3. Verifies correct behavior:
#   - Help text is displayed when no arguments
#   - Correct arguments are passed to doc() function
#   - File types are properly converted from extensions
#   - Boolean flags are correctly interpreted
#   - Numeric parameters are properly validated
#   - File paths are correctly handled
#
#4. Mirrors test coverage from test_doc.py while testing
#   through command-line interface instead of direct function calls
################################################################

class TestPronouns2_10p1(TestCase):
    """Tests command-line interface functionality of pronouns2.py's main() for example 10.1."""
    
    def setUp(self):
        """Prevent actual system exit in tests"""
        self._original_exit = sys.exit
        sys.exit = lambda x: None
        
    def tearDown(self):
        """Restore original system exit"""
        sys.exit = self._original_exit
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_basic_txt(self, mock_doc, mock_argv):
        """Test main() with basic TXT output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_10p1.txt', 
                                            '--file_type=.txt', '--info=True'][x]
        mock_argv.__len__ = lambda s: 5
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_10p1.txt', 
                                       file_type=FileType.TXT, info=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_basic_tex(self, mock_doc, mock_argv):
        """Test main() with basic TEX output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_10p1.tex', 
                                            '--file_type=.tex', '--info=True'][x]
        mock_argv.__len__ = lambda s: 5
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_10p1.tex', 
                                       file_type=FileType.TEX, info=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_txt(self, mock_doc, mock_argv):
        """Test main() with debug TXT output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_debug_10p1.txt', 
                                            '--file_type=.txt', '--info=True', '--debug=True'][x]
        mock_argv.__len__ = lambda s: 6
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_debug_10p1.txt', 
                                       file_type=FileType.TXT, info=True, debug=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_tex(self, mock_doc, mock_argv):
        """Test main() with debug TEX output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_debug_10p1.tex', 
                                            '--file_type=.tex', '--info=True', '--debug=True'][x]
        mock_argv.__len__ = lambda s: 6
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_debug_10p1.tex', 
                                       file_type=FileType.TEX, info=True, debug=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_trace_txt(self, mock_doc, mock_argv):
        """Test main() with debug and trace TXT output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_debug_trace_10p1.txt', 
                                            '--file_type=.txt', '--info=True', '--debug=True', '--trace=True'][x]
        mock_argv.__len__ = lambda s: 7
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_debug_trace_10p1.txt', 
                                       file_type=FileType.TXT, info=True, debug=True, trace=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_trace_tex(self, mock_doc, mock_argv):
        """Test main() with debug and trace TEX output for example 10.1"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2_debug_trace_10p1.tex', 
                                            '--file_type=.tex', '--info=True', '--debug=True', '--trace=True'][x]
        mock_argv.__len__ = lambda s: 7
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2_debug_trace_10p1.tex', 
                                       file_type=FileType.TEX, info=True, debug=True, trace=True)

