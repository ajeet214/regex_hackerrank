"""
Author : Ajeet
Date : 29/03/2023
"""
import re

n = int(input())
text = "\n".join(input() for _ in range(n))
t = int(input())
for _ in range(t):
    print(len(re.findall(f'\B{input()}\B',text)))