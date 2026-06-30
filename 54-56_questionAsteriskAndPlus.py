import re

pattern = r'Eggs( and spam)?'
#pattern = r'Eggs( and spam)*'
#pattern = r'Eggs( and spam)+'
messages = (
    'Eggs',
    'Eggs and spam',
    'Eggs and spam and spam'
)

pattern_obj = re.compile(pattern)
for message in messages:
    match_obj = pattern_obj.search(message)
    if match_obj:
        match = match_obj.group()
        print(match)
    else:
        print('None')
