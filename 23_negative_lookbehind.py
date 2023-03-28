"""
Author : Ajeet
Date : 28/03/2023

(?<!regex_2)regex_1
The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. Lookbehind is excluded
from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.

Task

You have a test String S.
Write a regex which can match all the occurences of characters which are not immediately
preceded by vowels (a, e, i, u, o, A, E, I, O, U).
"""

Regex_Pattern = r"(?<![aeiouAEIOU])."

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))