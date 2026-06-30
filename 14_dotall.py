import re

pattern = r'.*'
flag = re.DOTALL
message = '''\
Serve the public trust.
Protect the innocent.
Uphold the law.\
'''

#pattern_obj = re.compile(pattern)
pattern_obj = re.compile(pattern, flag)
match_obj = pattern_obj.search(message)
match = match_obj.group()
print(match)
