import re

pattern = r'.at'
message = '''/
The cat in the hat sat on the flat mat./
'''

pattern_obj = re.compile(pattern)
matches = pattern_obj.findall(message)
for match in matches:
    print(match)
