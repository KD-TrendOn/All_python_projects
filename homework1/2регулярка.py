import re
n = input()
ipv6 = re.compile('(([0-9]|[a-f]){4}:){7}([0-9]|[a-f]){4}')
print(bool(re.fullmatch(ipv6, n)))