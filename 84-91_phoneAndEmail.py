import pyperclip, re

phone_pattern = r'''(
    (\+\d{1,3}\s)?                # Country code
    (\d{3}|\(\d{3}\))?            # Area code
    [-.\s]?                       # Separator
    \d{3}                         # First three digits
    [-.\s]                        # Separator
    \d{4}                         # Last four digits
    (\s?(x|ext|ext\.)\s?\d{2,5})? # Extension
    )'''
email_pattern = r'''(
    [a-zA-Z0-9._%+-]+  # Username
    @                  # At sign
    [a-zA-Z0-9.-]+     # Domain name
    \.[a-zA-Z]{2,4}    # Top level domain
    (\.[a-zA-Z]{2,4})? # Second top level domain
    )'''
flag = re.VERBOSE
text = str(pyperclip.paste())

matches = []

# phone number search
phone_pattern_obj = re.compile(phone_pattern, flag)
phone_matches = phone_pattern_obj.findall(text)
matches.extend(match[0] for match in phone_matches)

# email address search
email_pattern_obj = re.compile(email_pattern, flag)
email_matches = email_pattern_obj.findall(text)
matches.extend(match[0] for match in email_matches)

# print and copy
if matches:
    print('Copied to clipboard:')
    for match in matches:
        print('', match)
    pyperclip.copy('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
