import re

pattern = r'dog|cat'
message = '''\
I have a cat. \
My friend has a dog.\
'''

pattern_obj = re.compile(pattern)
matches = pattern_obj.findall(message)
for match in matches:
    print(match)
