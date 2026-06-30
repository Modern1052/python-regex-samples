import re

pattern = r'''
    \d+      # Integer part
    (\.\d+)? # Decimal part
    '''
flag = re.VERBOSE
message = 'The temperature is 23.5 degrees.'

#pattern_obj = re.compile(pattern)
pattern_obj = re.compile(pattern, flag)
match_obj = pattern_obj.search(message)
if match_obj:
    match = match_obj.group()
    print(match)
else:
    print('None')
