import re

pattern = r'robocop'
flag = re.IGNORECASE
message = '''\
RoboCop is part man, \
part machine, all cop.\
'''

pattern_obj = re.compile(pattern, flag)
match_obj = pattern_obj.search(message)
match = match_obj.group()
print(match)
