"""
Task

You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters
"""

Regex_Pattern = r"(\S{2}\s){2}\S{2}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
