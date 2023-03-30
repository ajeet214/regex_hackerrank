"""
Author : Ajeet
Date : 30/03/2023
"""

import re

sentence = ' '.join(input() for _ in range(int(input())))

for _ in range(int(input())):
    print(len(re.findall(r'((?<=\W)|^)%s((?=\W)|$)' % input(), sentence)))