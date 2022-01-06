import re
print(bool(re.fullmatch(r'\d{4}/([1-9]|1[0-2])/([1-9]|[1-2]\d|3[0-1]) ([1-9]|1\d|2[0-3]):([1-9]|[1-5]\d)', input('input: '))))