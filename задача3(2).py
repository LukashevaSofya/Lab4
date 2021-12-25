def conversely(s):
    s = s.split()
    s.reverse()
    s2 = ' '.join(s)
    return s2
string = input()
string = conversely(string)
print(string)
