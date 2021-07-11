from itertools import permutations
S, k = map(str, input().split())
k = int(k)

A = sorted(list(permutations(S,k)))
for a in A:
    print(''.join(a))