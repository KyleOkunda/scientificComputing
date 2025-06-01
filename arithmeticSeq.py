n = 5
arr = [n]
c = 0

while c < 7:
    n += 3
    arr.append(n)
    c += 1

for e in arr:
    print(e, end=" ")