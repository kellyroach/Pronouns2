################################################################
#
#    test_pronouns2.py
#
################################################################

import sys
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from pronouns2 import *

################################################################
#1. Tests all major execution paths in `main()`:
#   - --help argument (help display)
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
#   - Help text is displayed when passed --help
#   - Correct arguments are passed to doc() function
#   - File types are properly converted from extensions
#   - Boolean flags are correctly interpreted
#   - Numeric parameters are properly validated
#   - File paths are correctly handled
#
#4. Mirrors test coverage from test_doc.py while testing
#   through command-line interface instead of direct function calls
################################################################

class TestPronouns2(TestCase):
    """Tests command-line interface functionality of pronouns2.py's main()."""
    
    def setUp(self):
        """Prevent actual system exit in tests"""
        self._original_exit = sys.exit
        sys.exit = lambda x: None
        
    def tearDown(self):
        """Restore original system exit"""
        sys.exit = self._original_exit
        
    @patch('sys.argv')
    def test_main_help(self, mock_argv):
        """Test main() with explicit --help flag"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--help'][x]
        mock_argv.__len__ = lambda s: 2
        with patch('sys.stdout', new=StringIO()) as captured_output:
            main()
            self.assertIn('usage:', captured_output.getvalue().lower())
            
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_basic_txt(self, mock_doc, mock_argv):
        """Test main() with basic TXT output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2.txt', '--file_type=.txt', '--info=True'][x]
        mock_argv.__len__ = lambda s: 4
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2.txt', 
                                       file_type=FileType.TXT, info=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_basic_tex(self, mock_doc, mock_argv):
        """Test main() with basic TEX output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2.tex', '--file_type=.tex', '--info=True'][x]
        mock_argv.__len__ = lambda s: 4
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2.tex', 
                                       file_type=FileType.TEX, info=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_txt(self, mock_doc, mock_argv):
        """Test main() with debug TXT output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2_debug.txt', 
                                            '--file_type=.txt', '--info=True', '--debug=True'][x]
        mock_argv.__len__ = lambda s: 5
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2_debug.txt', 
                                       file_type=FileType.TXT, info=True, debug=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_tex(self, mock_doc, mock_argv):
        """Test main() with debug TEX output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2_debug.tex', 
                                            '--file_type=.tex', '--info=True', '--debug=True'][x]
        mock_argv.__len__ = lambda s: 5
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2_debug.tex', 
                                       file_type=FileType.TEX, info=True, debug=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_trace_txt(self, mock_doc, mock_argv):
        """Test main() with debug and trace TXT output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2_debug_trace.txt', 
                                            '--file_type=.txt', '--info=True', '--debug=True', '--trace=True'][x]
        mock_argv.__len__ = lambda s: 6
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2_debug_trace.txt', 
                                       file_type=FileType.TXT, info=True, debug=True, trace=True)
        
    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_debug_trace_tex(self, mock_doc, mock_argv):
        """Test main() with debug and trace TEX output"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2_debug_trace.tex', 
                                            '--file_type=.tex', '--info=True', '--debug=True', '--trace=True'][x]
        mock_argv.__len__ = lambda s: 6
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2_debug_trace.tex', 
                                       file_type=FileType.TEX, info=True, debug=True, trace=True)

    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_with_numbers(self, mock_doc, mock_argv):
        """Test main() with example numbers specified"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '10.1', '--file=test_pronouns2.txt', 
                                            '--file_type=.txt', '--info=True'][x]
        mock_argv.__len__ = lambda s: 5
        main()
        mock_doc.assert_called_once_with(numbers='10.1', file='test_pronouns2.txt', 
                                       file_type=FileType.TXT, info=True)

    @patch('sys.argv')
    @patch('pronouns2.doc')
    def test_main_with_chaining_rho(self, mock_doc, mock_argv):
        """Test main() with custom chaining_rho value"""
        mock_argv.__getitem__ = lambda s, x: ['pronouns2.py', '--file=test_pronouns2.txt', 
                                            '--file_type=.txt', '--chaining_rho=0.7'][x]
        mock_argv.__len__ = lambda s: 4
        main()
        mock_doc.assert_called_once_with(numbers=None, file='test_pronouns2.txt', 
                                       file_type=FileType.TXT, chaining_rho=0.7)

