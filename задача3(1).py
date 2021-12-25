
def conversely(s):
    s2 = ''
    i = len(s)-1
    while i >= 0:
        if s[i] == ' ':
            s2 = s2 + s[i+1:] + ' '
            s = s[:i]
            i = len(s) - 1
        else:
            i -= 1
    s2 = s2 + s
    return s2
 
string = input()
string = conversely(string)
print(string)

