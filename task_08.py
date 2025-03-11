import re
def multiply_numbers(inputs = None):
    op = 1
    inputs = str(inputs)

    y = re.sub(r'\D', '', inputs.lower())

    if len(y) == 0:
        return None

    for i in y:
        op = op * int(i)

    return op


num_started = 2.4
x = multiply_numbers(num_started)
print(x)