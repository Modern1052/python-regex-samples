import re

pattern = r'\d+\s\w+'
message ='''\
12 drummers, 11 pipers, 10 lords, \
9 ladies, 8 maids, 7 swans, ...\
'''

pattern_obj = re.compile(pattern)
matches = pattern_obj.findall(message)
for match in matches:
    print(match)
