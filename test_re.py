import re

with open("./test_00.py", "r") as f:
    text_00 = f.read()
print(re.findall("sort", text_00))