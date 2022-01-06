import re
print(bool(re.fullmatch(r'(([0-9]|[A-F]){2}:){5}([0-9]|[A-F]){2}', input('mac adress: '))))