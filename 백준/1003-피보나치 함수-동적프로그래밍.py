T = int(input())

zero_dict = {0:1, 1:0, 2:1}
one_dict = {0:0, 1:1, 2:1}


for t in range(T):
    N = int(input())
    if N in zero_dict:
        print("%d %d" %(zero_dict[N], one_dict[N]))
    else:
        for x in range(len(zero_dict), N+1):
            zero_dict[x] = zero_dict[x-1] + zero_dict[x-2]
            one_dict[x] = one_dict[x-1]+one_dict[x-2]
        print("%d %d" %(zero_dict[N], one_dict[N]))


