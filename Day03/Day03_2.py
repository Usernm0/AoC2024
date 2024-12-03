import re

a = text.replace('\n', "").split("do()")
total = 0
x = ""

for e in a:
    e = re.sub("don't\\(\\).*", "", e)
    x += e
x = re.findall("mul\\([\\d]+\\,[\\d]+\\)", x)

for item in x:
    a, b = item.lstrip("mul(").rstrip(")").split(",")
    total += int(a) * int(b)
print(total)