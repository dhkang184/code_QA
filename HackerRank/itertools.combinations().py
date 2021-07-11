from itertools import combinations

S, k = map(str, input().split())
k = int(k)

for i in range(1,k+1):
    c_list = sorted(list(combinations(sorted(S),i)))
    for c in c_list:
        print(''.join(c))