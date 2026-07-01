from humre import *

pattern = group(
    exactly(3, DIGIT),
    '-',
    exactly(3, DIGIT),
    '-',
    exactly(4, DIGIT)
    )
message = 'My number is 415-555-4242'

pattern_obj = re.compile(pattern)
match_obj = pattern_obj.search(message)
match = match_obj.group()
print(match)
