#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
# 00:05~ 00:45

def solution(n, k, S):

    rotat = (n//4)
    list_s = [s for s in S]
    new_s = list_s + list_s[:rotat]
    ans_list = []
    for idx in range(n):
        ans_list.append(int("".join(new_s[idx: idx+rotat]), 16))
        #ans_list.append("".join(new_s[idx: idx + rotat]))

    return(sorted(list(set(ans_list)), reverse=True)[k-1])

T = int(input())
for _idx in range(1, T+1):
    n , k = map(int,input().split())
    S = input()
    ans = solution(n, k, S)
    print(("#%d %d" %(_idx, ans)))


