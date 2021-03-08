#https://programmers.co.kr/learn/courses/30/lessons/42577
#시작시간: 22:35

def solution(phone_book):

    phone_book.sort()
    answer = True
    for x,y in zip(phone_book, phone_book[1:]):
        if y.startswith(x):
            answer = False
            break
    return(answer)

""" 풀이 2
def solution(phone_book):

    answer = True
    di_p = [[] for _ in range(10)]
    #sort_p = sorted(phone_book)
    for x in phone_book:
        di_p[int(x[0])-1].append(x)

    for sort_x in di_p:
        sort_x.sort()
        for idx, x in enumerate(sort_x[:-1]): #x: 앞자리 별 리스트
            if len(x) == len(sort_x[-1]):
                continue
            if x ==  sort_x[idx+1][:len(x)]:
                return False
    return answer
"""
"""
def solution(phone_book):
    answer = True
    sort_p = sorted(phone_book)

    for idx,p in enumerate(sort_p[:-1]):
        for x in sort_p[idx+1:]:
            if p == x[:len(p)]:
                return False

    return answer
"""
solution(["12","123","1235","567","88"])