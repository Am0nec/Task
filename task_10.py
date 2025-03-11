import re
from collections import defaultdict

def count_words(string):

    string = string.lower()

    string = re.sub(r'[^\w\s]', '', string)

    words = string.split()

    word_count = defaultdict(int)

    for word in words:
        word_count[word] += 1
    return dict(word_count)


x = count_words("A man, a plan, a canal -- Panama")
print(x)
