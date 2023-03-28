"""
Author : Ajeet
Date : 28/03/2023

regex_1(?=regex_2)
The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. The lookahead is excluded from
the match. It does not return matches of regex_2. The lookahead only asserts whether a match is possible or not.

Task

You have a test string S.
Write a regex that can match all occurrences of o followed immediately by oo in S.
"""

Regex_Pattern = r'o(?=oo)'

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

print(str(bool(re.search(Regex_Pattern, input()))).lower())
