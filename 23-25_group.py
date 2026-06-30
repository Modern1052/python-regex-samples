import re

pattern = r'(\d{3})-(\d{3}-\d{4})'
message = 'My number is 415-555-4242.'

pattern_obj = re.compile(pattern)
match_obj = pattern_obj.search(message)
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2))
print(match_obj.groups())
