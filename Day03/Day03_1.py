import re

text.replace('\n', "")
text2 = re.sub("don't\\(\\).*?do\\(\\)", "", text)
x = re.findall("mul\\([\\d]+\\,[\\d]+\\)", text2)
total = 0

for item in x:
    a, b = item.lstrip("mul(").rstrip(")").split(",")
    total += int(a) * int(b)
    #print(a, b)
print(total)