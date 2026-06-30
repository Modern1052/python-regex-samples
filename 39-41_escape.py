import re

#pattern = r'(\d{3})\d{3}-\d{4}'
pattern = r'\(\d{3}\)\d{3}-\d{4}'
message = 'My number is (415)555-4242.'

pattern_obj = re.compile(pattern)
match_obj = pattern_obj.search(message)
if match_obj:
    match = match_obj.group()
    print(match)
else:
    print('None')
