import unittest

class FloatAssertionMixin:
    """Mixin class providing additional float-related assertions for unittest.TestCase"""
    
    def assertListAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        """
        Assert that two lists of floats are almost equal within specified precision.
        
        Args:
            first: First list of floats to compare
            second: Second list of floats to compare
            places: Number of decimal places to compare (default 7 if delta is None)
            msg: Custom error message to show on failure
            delta: Maximum difference allowed between values
        Raises:
            AssertionError: If lists differ in length or if any elements aren't almost equal
        """
        # Check if inputs are lists/sequences
        if not hasattr(first, '__iter__') or not hasattr(second, '__iter__'):
            raise TypeError("Inputs must be iterable")
            
        # Check lengths match
        if len(first) != len(second):
            standardMsg = f'Lists have different lengths: {len(first)} != {len(second)}'
            msg = self._formatMessage(msg, standardMsg)
            raise AssertionError(msg)
        
        # Compare elements
        for i, (a, b) in enumerate(zip(first, second)):
            try:
                self.assertAlmostEqual(a, b, places=places, delta=delta)
            except AssertionError as e:
                standardMsg = f'Lists differ at index {i}: {a} != {b}'
                if msg is None:
                    msg = standardMsg
                else:
                    msg = f'{msg}\n{standardMsg}'
                raise AssertionError(msg) from e
    
    def assertNotListAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        """
        Assert that two lists of floats are NOT almost equal within specified precision.
        Lists are considered not almost equal if they have different lengths or if any
        corresponding elements are not almost equal.
        
        Args:
            first: First list of floats to compare
            second: Second list of floats to compare
            places: Number of decimal places to compare (default 7 if delta is None)
            msg: Custom error message to show on failure
            delta: Maximum difference allowed between values
        Raises:
            AssertionError: If lists are almost equal
        """
        if not hasattr(first, '__iter__') or not hasattr(second, '__iter__'):
            raise TypeError("Inputs must be iterable")
            
        # Different lengths mean not equal
        if len(first) != len(second):
            return
            
        # Check if ALL elements are almost equal
        all_equal = True
        try:
            for a, b in zip(first, second):
                try:
                    self.assertAlmostEqual(a, b, places=places, delta=delta)
                except AssertionError:
                    all_equal = False
                    break
        except TypeError:
            all_equal = False
            
        # If all elements were almost equal, that's a failure for NotAlmostEqual
        if all_equal:
            standardMsg = (f'Lists are almost equal within specified precision '
                          f'(places={places}, delta={delta})')
            msg = self._formatMessage(msg, standardMsg)
            raise AssertionError(msg)
