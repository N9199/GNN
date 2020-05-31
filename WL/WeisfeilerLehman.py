import numpy as np
from sys import stderr


n, k = list(map(int, input().split()))
c = int(input())
cols = list(map(int, input().split()))

G = (n ** k) * [None]
color = (n ** k) * [None]

for i in range(n ** k):
    color[i] = np.zeros(c, dtype=int)
    color[i][cols[i]] = 1
    G[i] = k * [None]
    for j in range(k):
        G[i][j] = []

for j in range(k * (n ** k)):
    s = list(map(int, input().split()))
    G[j//k][s[0]] = s[1:]
print("Start Counting", file=stderr)
for _ in range(n ** k):
    print("Iteration: {}".format(_), file=stderr)
    temp = (n ** k) * [None]
    for i in range(n ** k):
        temp[i] = k * [None]
        for j in range(k):
            temp[i][j] = np.zeros(c, dtype=int)
            for e in G[i][j]:
                temp[i][j] += color[e]

    for i in range(n ** k):
        color[i] += sum(temp[i])

print(len(color))
print('\n'.join(map(lambda x: ' '.join(map(str, x)), color)))
print()
