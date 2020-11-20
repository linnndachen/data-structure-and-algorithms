import unittest

def one_away(s1, s2):
    """
    > Description: check if s1 and s2 is 1 edit away from each other. The edits can be insert, remove or replace.
    > Input: String
    > Output: Boolean
    """
    #if it is an empty string with a string with only 1 character or 2 string are the same, return true
    if len(s1) and len(s2) <=1 or s1==s2:
        return True

    #if the difference is bigger than 2
    if abs(len(s1)-len(s2))>1:
        return False
    else: 
    #find the different character of the string string and then compare their positions
        edited = False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False
                edited = True
                if len(s1) < len(s2):
                    j += 1
                elif len(s1) > len(s2):
                    i += 1
                else:
                    i += 1
                    j += 1
    return True

print(one_away('pale', 'ble'))

def one_away_seperate(s1, s2):
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_insert(s2, s1)
    return False

def one_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

def one_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]
    def test_one_away_seperate(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away_seperate(test_s1, test_s2)
            print(actual, test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
