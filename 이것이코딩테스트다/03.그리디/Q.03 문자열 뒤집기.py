def solution():
    S = input()
    result = 0
    start_s = S[0]
    before_s = S[0]
    for x in S:
        if x != start_s and x != before_s :
            result +=1
        before_s = x
    print(result)

solution()

def book_solution():
    S = input()
    count0 = 0 #모두 0으로 바꾸는 횟수
    count1 = 0 #모두 1로 바꾸는 횟수

    if S[0] == "0":
        count1 +=1
    else:
        count0 +=1

    for i in range(len(S) -1):
        if S[i] != S[i+1]:
            if S[i+1] == '1':
                count1 +=1
            else:
                count0 +=1
    print(min(count0,count1))