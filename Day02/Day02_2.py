count = 0

def check_line(line):
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
    return safe

for line in text.rstrip('\n').split('\n'):
    line = [int(item) for item in line.split()]
    if check_line(line):
        count += 1
        continue
    for i in range(len(line)):
        nline = line.copy()
        del nline[i]
        if check_line(nline):
            count += 1
            break
print(count)