#This question is position + counts


import unittest
from collections import Counter

"""
Previous Solution:
def string_compression(s):
    res = ''
    v = 1
    for i in range(1, len(s)):
        if s[i]!= s[i-1]:
            res = res+str(s[i-1])+str(v)
            v = 1
        else:
            v+=1
    #append the last group
    res = res+str(s[i-1])+str(v)
    if len(res) >= len(s):
        return s
    return res

This is inefficient because "string concatenation requires all characters to be copied, this is a O(N+M) operation (where N and M are the sizes of the input strings). M appends of the same word will trend to O(M^2) time therefor." (0+1) + (1+1) +...+ m = m(m+1)/2 = O(m^2)
"""
def string_compression(s):
    compressed = []
    v = 1
    for i in range(1, len(s)):
        if s[i]!= s[i-1]:
            compressed.append(s[i-1])
            compressed.append(str(v))
            v = 1
        else:
            v+=1
    #append the last group
    compressed.append(s[i-1])
    compressed.append(str(v))
    return min(s, ''.join(compressed), key=len)



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
