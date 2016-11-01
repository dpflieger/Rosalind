# INI1. Installing python
import this # zen of python

# INI2. Variables and some arithmetic
def hypotenuse(a, b):
    return a ** 2 + b ** 2

# INI3. Strings and lists
def slicing(string, a, b, c, d):
    print((string[a:b+1], " ", string[c:d+1]))

# INI4. Conditions and loops
def sum_odd_from_range(a, b):
    print(sum(range(a|1, b+1, 2)))

# INI5. Working with files
def get_odd_line(file):
    with open(file, "r") as f:
        [print(odd_line) for odd_line in f.readlines[1::2]]

# INI6. Dictionaries
from collections import Counter
text ="We tried list and we tried dicts also we tried Zen"
[print(k, v) for k, v in Counter(text.split()).items()]
