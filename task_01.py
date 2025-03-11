import re
def is_palindrome(string):
    y = re.sub(r'\W', '', string.lower())
    if len(y) == 0:
        return False
    elif y == y[::-1]:
        return True
    else:
        return False

z = "A man, a plan, a canal -- Panama"
x = is_palindrome(z)
print(x)