import re
pattern = r'\d{3}-\d{3}-\d{4}'
message = '''\
Call me at 415-555-1011 tomorrow. \
415-555-9999 is my office.\
'''

pattern_obj = re.compile(pattern)
matches = pattern_obj.findall(message)
for match in matches:
    print(match)
