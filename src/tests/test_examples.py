################################################################
#
#    test_examples.py
#
################################################################

from unittest import TestCase
from pronouns2 import *

def csn_integrity(number, csn) -> int:
    """Test csn list-str representation integrity"""
    bad = 0
    if isinstance(csn, str):
        pass
    elif isinstance(csn, list):
        if len(csn) == 0:
            bad += 1
            print(f"{number}: Error: len == 0")
            print(f"    {csn}")
        else:
            parent = csn[0]
            if (parent != "C") and (parent != "S"):
                bad += 1
                print(f"{number}: Error: neither 'C' nor 'S'")
                print(f"    {parent}")
            for child in csn[1:]:
                bad += csn_integrity(number, child)
    else:
        bad += 1
        print(f"{number}: Error: {type(csn)}: isn't str nor list")
        print(f"    {csn}")
    return bad

class TestExamples(TestCase):
    def test_examples_negative_integrity(self):
        """I want to see a negative before I provide you with a positive."""
        # "A type II error corresponds to acquitting a criminal." -- Wikipedia
        # This test checks csn_integrity's ability to convict criminals.
        bad = 0
        number = "#IGNORE"
        bad += csn_integrity(number, 123)
        bad += csn_integrity(number, [])
        bad += csn_integrity(number, ["X"])
        bad += csn_integrity(number, ["S", ["John"], ["Mary"]])
        if bad > 0:
            # Not an "Error:".  This test is supposed to detect mistakes.
            print(f"{number}: {bad} mistakes detected.")
        self.assertEqual(bad, 5)
    def test_examples_integrity(self):
        """Test example_dict integrity"""
        # Verifies all the ex's in example_dict have expected form.
        bad = 0
        for number, ex in example_dict.items():
            if not isinstance(ex, list):
                bad += 1
                print(f"{number}: Error: not a list")
                print(f"    {ex}")
            elif len(ex) != 2:
                bad += 1
                print(f"{number}: Error: len != 2")
                print(f"    {ex}")
            else:
                sentence = ex[0]
                csn = ex[1]
                if not isinstance(sentence, str):
                    bad += 1
                    print(f"{number}: Error: not a str")
                    print(f"    {sentence}")
                bad += csn_integrity(number, csn)
        if bad > 0:
            print(f"Error: {bad} mistakes detected.")
        # Save the single potentially hard failure assertion for last,
        # so that test_examples_integrity can print as much damaging
        # information as possible in its report before rejecting us.
        self.assertEqual(bad, 0)
    def rejected_test_examples_distinct(self):
        """Test examples are distinct"""
        # This test works "too well" for our 1980 M.S. thesis examples:
        # "Error: 9 duplicates detected."  We'll leave its code here,
        # but we don't use it nor need to pass it.
        bad = 0
        seen = []
        for number, ex in example_dict.items():
            if ex in seen:
                # The test detects duplicate ex's.  We've decided we're
                # not going to check for duplicate sentence's, which
                # might be legitimately ambiguous with different parse
                # tree structures.
                bad += 1
                print(f"Error: ({number}) duplicates earlier example.")
                print(f"    {ex}")
            else:
                seen.append(ex)
        if bad > 0:
            print(f"Error: {bad} duplicates detected.")
        self.assertEqual(bad, 0)
