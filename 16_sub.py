import re

pattern = r'Agent (\w)\w+'
replacement = 'CENSORED'
#replacement = r'\1****'
message = 'Agent Alice contacted Agent Bob.'

pattern_obj = re.compile(pattern)
replaced_message = pattern_obj.sub(replacement, message)
print(replaced_message)
