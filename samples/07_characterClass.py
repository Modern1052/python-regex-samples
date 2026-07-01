import re

pattern = r'[aeiouAEIOU]'
#pattern = r'[^aeiouAEIOU]'
#pattern = r'[a-zA-Z]'
message = 'RoboCop eats BABY FOOD.'

pattern_obj = re.compile(pattern)
matches = pattern_obj.findall(message)
for match in matches:
    print(match, end = ' ')
