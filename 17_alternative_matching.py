"""
Author : Ajeet
Date : 28/03/2023

Task

Given a test string, s, write a RegEx that matches s under the following conditions:

s must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
"""

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
