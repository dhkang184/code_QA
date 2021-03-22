#https://programmers.co.kr/learn/courses/30/lessons/42746
# 23:30~ 24:30

def solution(numbers):
    str_n = sorted(map(str,numbers))
    if str_n[-1] =="0":
        return "0"
    n_array = ["0"] * len(numbers)
    n_array[0] = str_n[-1]
    str_n.pop()
    last_idx = 0
    while str_n:
        if n_array[last_idx] + str_n[-1] >= str_n[-1] + n_array[last_idx]:
            last_idx +=1
            n_array[last_idx] = str_n[-1]
            str_n.pop()
        else:
            minus_idx = 1
            while True:
                if n_array[last_idx - minus_idx] + str_n[-1] >= str_n[-1] +n_array[last_idx-minus_idx]:
                    break
                else:
                    minus_idx +=1
                if minus_idx >= last_idx:
                    break
            for y in range(minus_idx):
                n_array[last_idx-y+1] = n_array[last_idx-y]
            n_array[last_idx-y] = str_n[-1]
            str_n.pop()
            last_idx +=1

    answer = ''.join(n_array)

    return answer


print(solution(	[3, 30, 34, 5, 9, 0, 0 ,10,11,15, 101]))