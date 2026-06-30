import re

#pattern = r'\d+'
pattern = r'^\d+'
#pattern = r'\d+$'
messages = (
    'I have 3 cats.',
    '10 years ago, ...',
    'password : 2336'
)

pattern_obj = re.compile(pattern)
for message in messages:
    match_obj = pattern_obj.search(message)
    if match_obj:
        match = match_obj.group()
        print(match)
    else:
        print('None')
