import re
n = input('Введите строку')
ip4 = re.compile('((\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|\d\d|1\d\d|2[0-4]\d|25[0-5])')
print(bool(re.fullmatch(ip4, n)))