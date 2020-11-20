
#Note: is it possible to have O(1)?

import unittest

from collections import Counter

#O(n)
def pal_perm(s):
    """
    check if the string is a permutation of a palidrome.
    The palidrome can be randome words.
    """
    s = s.replace(" ", "").lower()
    c = Counter(s)
    single = []
    for k, v in c.items():
        if v%2 != 0:
            single.append(k)
        if len(single) > 1:
            return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    """
    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)
    """

"""
if __name__ == "__main__":
    unittest.main()
"""