import numpy as np

from copy import deepcopy


def f(x):
    if x == 0:
        return 0
    if x % 2:
        return 1 - f(x // 2)
    return f(x // 2)


# Assumes graph is 3-regular
l = int(input())
n, m = list(map(int, input().split()))
k = 3
G = n * [None]
for i in range(n):
    G[i] = []
for _ in range(m):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)
for i in range(n):
    G[i].sort()
t = int(input())

X = (2 * k + (2 ** (k - 1))) * [None]
for i in range(2 * k + (2 ** (k - 1))):
    X[i] = []

for i in range(2**k):
    if f(i) == 1:
        continue
    for j in range(k):
        if (i >> j) % 2:
            X[j].append(2 * k + i // 2)
            X[2 * k + i // 2].append(j)
        else:
            X[k + j].append(2 * k + i // 2)
            X[2 * k + i // 2].append(k + j)

G1 = (n * len(X)) * [None]
G2 = (n * len(X)) * [None]
for u in range(n):
    G1[len(X) * u: len(X) * (u + 1)] = deepcopy(X)
    G2[len(X) * u: len(X) * (u + 1)] = deepcopy(X)
    for i in range(len(X) * u, len(X) * (u + 1)):
        for j in range(len(G1[i])):
            G1[i][j] += len(X) * u
            G2[i][j] += len(X) * u

# Solucionar problema entero:
# Dado un grafo 3-regular G
# A cada arista e se le asignan 3 variables, a_e, b_e y c_e,
# tal que a_e+b_e+c_e=1
# Además, dado un nodo u, la suma de los a_(u,v) es 1,
# idem con los b_(u,v) y c_(u,v)

"""
x = cp.Variable(k * (k * n), bool=True)
A = np.zeroes((2 * k * n, k * (k * n)))

for i in range(k * n):
    pass """


edges = []
for u in range(n):
    for v in G[u]:
        if v < u:
            continue
        edges.append([u, v, None])

"""
def func(i):
    if i == len(edges):
        return
    temp1 = list(edges[i][:2])
    temp1.sort()
    for j in range(k):
        flag = True
        for e in range(i):
            temp2 = list(edges[e][:2])
            temp2.sort()

"""

c = 0
flag = True
for i in range(len(edges)):
    edges[i][2] = c
    if flag:
        c += 1
    else:
        c -= 1
    if flag and c == 3:
        c -= 1
        flag = False
    if not flag and c == 0:
        c += 1
        flag = True


flag = True
for u, v, i in edges:
    if v < u:
        continue
    G1[len(X) * u + i].append(len(X) * v + i)
    G1[len(X) * u + k + i].append(len(X) * v + k + i)
    G1[len(X) * v + i].append(len(X) * u + i)
    G1[len(X) * v + k + i].append(len(X) * u + k + i)
    if flag:  # Twist one edge
        G2[len(X) * u + i].append(len(X) * v + k + i)
        G2[len(X) * u + k + i].append(len(X) * v + i)
        G2[len(X) * v + i].append(len(X) * u + k + i)
        G2[len(X) * v + k + i].append(len(X) * u + i)
        flag = False
    else:
        G2[len(X) * u + i].append(len(X) * v + i)
        G2[len(X) * u + k + i].append(len(X) * v + k + i)
        G2[len(X) * v + i].append(len(X) * u + i)
        G2[len(X) * v + k + i].append(len(X) * u + k + i)

print(len(X)*n, len(edges)+n*k*(2**(k-1)))
print(l)
if t == 2:
    G1, G2 = G2, G1
for u in range(len(X) * n):
    for v in G1[u]:
        if v < u:
            continue
        print(u, v)
