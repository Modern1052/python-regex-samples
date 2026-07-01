import re

#pattern = r'(Ha){3,5}'
pattern = r'(Ha){3,5}?'
#pattern = r'(Ha)+'
#pattern = r'(Ha)+?'
message = 'HaHaHaHaHaHa'

pattern_obj = re.compile(pattern)
match_obj = pattern_obj.search(message)
match = match_obj.group()
print(match)
