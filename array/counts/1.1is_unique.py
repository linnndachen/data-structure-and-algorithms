import unittest

#O(1) but needs memory
def unique_1(s1):
    dic = dict()
    for s in s1:
        if s in dic:
            return False
        else:
            dic[s]=1
    return True

#O(1) and do not need memory space
def unique(s1):
    u = set(s1)
    return len(u) == len(s1)

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()