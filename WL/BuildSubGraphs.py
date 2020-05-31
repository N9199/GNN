# Input
# n: Number of nodes of G
# m: Number of edges of G
# k: The dimension of the induced graph
# G: as a list of edges

# Output
# k-G: The k-th dimensional induced subgraph as a list of edges
# Colors: A list of colors of each node in k-G

# Note: nodes are 0-indexed

from collections import OrderedDict

n, m = list(map(int, input().split()))
k = int(input())

G = n * [None]
for i in range(n):
    G[i] = []

for i in range(m):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)

outG = (n ** k) * [None]
for i in range(n**k):
    outG[i] = k * [None]
    for j in range(k):
        outG[i][j] = []

inducedGraphs = (n ** k) * [None]
colors = (n**k)*[None]

curr = (n ** k) * [None]
# It isn't the most efficient way, should reuse info between constructions
for i in range(n ** k):
    curr[i] = k * [0]
    if i > 0:
        curr[i][0] += 1
        for j in range(k):
            curr[i][j] += curr[i-1][j]
    if i > 0 and i % n == 0:
        for j in range(k):
            if curr[i][j] == n:
                curr[i][j] = 0
                if j+1 < n:  # Should always evaluate to True
                    curr[i][j + 1] += 1

    temp = set(curr[i])
    inducedGraphs[i] = n * [None]
    for j in range(n):
        inducedGraphs[i][j] = []
    for u in temp:
        for v in G[u]:
            if v in temp:
                inducedGraphs[i][u].append(v)

c = 0
for i in range(n ** k):
    if colors[i] is not None:
        continue
    colors[i] = c
    temp = set(curr[i])
    for j in range(i + 1, n ** k):
        flag = True
        if len(temp) != len(set(curr[j])):
            continue
        f = dict(zip(curr[j], curr[i]))
        for l in range(k):
            if len(inducedGraphs[i][curr[i][l]]) != len(inducedGraphs[j][curr[j][l]]):
                flag = False
                break
            for e in inducedGraphs[j][curr[j][l]]:
                if f[e] not in temp:
                    flag = False
                    break

        if flag:
            colors[j] = c
    c += 1

for i in range(n ** k):
    for j in range(i+1, n ** k):
        index = -1
        for l in range(k):
            if curr[i][l] != curr[j][l]:
                if index == -1:
                    index = l
                else:
                    index = -1
                    break
        if index != -1:
            outG[i][index].append(j)
            outG[j][index].append(i)
print(n, k)
print(c)
print(' '.join(map(str, colors)))
print('\n'.join(map(lambda x: '\n'.join(map(lambda y: ' '.join(
    map(str, y)), map(lambda z: [z[0]]+z[1], enumerate(x)))), outG)))
