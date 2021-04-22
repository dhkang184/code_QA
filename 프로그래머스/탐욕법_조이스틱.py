#https://programmers.co.kr/learn/courses/30/lessons/42860
# 23:05~ 23:42

def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]
    answer = 0
    where = 0
    while True:
        answer += m[where]
        m[where] = 0
        if sum(m) == 0:
            break
        left, right = (1,1)
        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1
        answer += left if left < right else right
        where += -left if left < right else right
    return answer


# def solution(name):
#     temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     dic = dict(zip(temp, range(len(temp))))
#     dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
#     answer = dic[name[0]]
#     right_A =0
#     left_A =0
#
#
#     for x in range(1, len(name)):
#         if dic[name[x]] >0:
#             break
#         if x == len(name) -1:
#             return 0
#         right_A +=1
#
#     for x in range(1, len(name)):
#         if dic[name[-x]] >0:
#             break
#         left_A +=1
#
#     if left_A >= right_A:
#         for x in range(1, len(name) -left_A):
#             answer += dic[name[x]] +1
#     else:
#         for x in range(1, len(name) -right_A):
#             answer += dic[name[-x]] +1
#
#     return answer


print(solution("AAA"))