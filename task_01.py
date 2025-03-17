import re
def is_palindrome(string):
    s = str(string)
    if len(s) == 0:
        return False
    y = re.sub(r'\W', '', s.lower())
    if len(y) == 0:
        return False
    elif y == y[::-1]:
        return True
    else:
        return False

z = 333
x = is_palindrome(z)
print(x)
