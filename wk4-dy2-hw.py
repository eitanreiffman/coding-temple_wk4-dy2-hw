# Regex project
# Use Python to read the file regex_test.txt and print the first and last name on each line using regular expressions and groups
# (Return None for names with no first and last name, or names that aren't properly capitalized)
# Hint: use with open() and readlines()
"""
Expected Output:
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""
import re

file = open('regex_test.txt')
data = file.read()
# print(data)

pattern = re.compile("([A-Z][a-z]+\s)(?P<middle_name>[A-Z][a-z]*[ ])*(?P<last_name>[A-Z][a-z]+)")
get_pattern = pattern.finditer(data)
# print(get_pattern)

for name in get_pattern:
    if name.group("middle_name"):
        print(name.group("middle_name"),name.group("last_name"))
    else:
        print(name.group("last_name"))