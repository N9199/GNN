n = int(input())
d = {}
for _ in range(n):
    temp = tuple(list(map(int, input().split())))
    if temp in d:
        d[temp] += 1
    else:
        d[temp] = 1
out = list(d.values())
out.sort()
print(' '.join(map(str, out)))
