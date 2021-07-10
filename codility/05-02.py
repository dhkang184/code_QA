# 10:15~

def solution(S,P,Q):
    R = []
    Num_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    count_T = [[0]*(len(S)+1) for _ in range(4)]
    for idx, item in enumerate(S):
        count_T[0][idx+1] = count_T[0][idx]
        count_T[1][idx+1] = count_T[1][idx]
        count_T[2][idx+1] = count_T[2][idx]
        count_T[3][idx+1] = count_T[3][idx]
        count_T[Num_dict[item]][idx+1] +=1

    for i in range(len(P)):
        for j in range(4):
            if count_T[j][Q[i]+1] - count_T[j][P[i]] >0:
                R.append(j+1)
                break

    return R