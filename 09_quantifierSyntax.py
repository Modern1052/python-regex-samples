import re

pattern = r'\d{2}'
#pattern = r'\d{2,4}'
#pattern = r'\d{2,}'
messages = (
    '1',
    '12',
    '123',
    '1234',
    '12345',
    '123456'
)

pattern_obj = re.compile(pattern)
for message in messages:
    matches = pattern_obj.findall(message)
    if matches:
        print(' '.join(matches))
    else:
        print('None')
