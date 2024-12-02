count = 0
for line in text.rstrip('\n').split('\n'):
    line = [int(item) for item in line.split()]
    asc = True
    desc = True
    safe = True
    for i in range(len(line) - 1):
        dir = line[i] - line[i + 1]
        if dir > 0:
            asc = False
        if dir < 0:
            desc = False
        if dir > 3 or dir < -3 or dir == 0 or (asc == False and desc == False):
            safe = False
        if safe == False:
            break
    if safe == True:
        count += 1
print(count)    