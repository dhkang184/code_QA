#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx in range(len(phone_book)):
        cur = phone_book[idx]
        for check in phone_book[idx+1:]:
            if cur == check[:len(cur)]:
                return False
    return answer