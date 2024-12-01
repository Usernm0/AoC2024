a, b, c = [], [], []

for line in text.rstrip('\n').split('\n'):
    n1, n2 = line.split('   ')
    a.append(int(n1))
    b.append(int(n2))
a.sort()
b.sort()
for i in range(0, len(a)):
    c.append(a[i] * b.count(a[i]))
print(sum(c))