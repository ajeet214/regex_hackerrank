"""
Author : Ajeet
Date : 24/03/2023

Task

You have a test string S.
Your task is to write a regex that will match S with following conditions:

S must be of length: 6
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
"""
Regex_Pattern = r'^[123][012][xs0][30Aa][xsu][,\.]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
