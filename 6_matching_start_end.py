"""
Author : Ajeet
Date : 24/03/2023

Task

You have a test string S. Your task is to match the pattern Xxxxx.
Here, x denotes a word character, and X denotes a digit.
S must start with a digit X and end with . symbol.
S should be 6 characters long only.
"""

Regex_Pattern = r"^\d.{4}\.$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
