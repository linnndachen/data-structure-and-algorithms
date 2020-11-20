
def is_substring(string, sub):
    #check if s2 is the rotation of s1
    return string.find(sub) != -1

#if we do not use s.find() in python
def find_str(s, sub):
    index = 0

    if sub in s:
        c = sub[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(sub)] == sub:
                    return index

            index += 1

    return -1

def string_rotation(s1, s2):
    """
    check if s2 is a rotation of s1
    """
    if len(s1) == len(s2) != 0:
        return is_substring(s1+s1, s2)
    return False

print(string_rotation('waterbottle', 'erbottlewat'))