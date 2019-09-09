T = int(input())
N_dict = {1:1, 2:2, 3:4 }
def F_next(N):
    if N in N_dict:
        return N_dict[N]

    for idx in range(len(N_dict) +1, N+1):
        N_dict[idx] = N_dict[idx-1] + N_dict[idx-2] + N_dict[idx-3]

    return N_dict[N]

for idx in range(T):
    N = int(input())
    print(F_next(N))




