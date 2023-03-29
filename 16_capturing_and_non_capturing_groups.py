"""
Author : Ajeet
Date : 28/03/2023

Parenthesis ( ) around a regular expression can group that part of regex together.
(?: ) can be used to create a non-capturing group. It is useful if we do not need the group to capture its match.

Task

You have a test String S.
Your task is to write a regex which will match S with the following condition:

S should have 3 or more consecutive repetitions of ok.
"""

Regex_Pattern = r'(ok){3,}'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
