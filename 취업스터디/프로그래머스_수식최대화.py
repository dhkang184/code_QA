
def solution(expression):
    answer = 0

    def cal(P, num_list1, p_list1):
        num_list = [x for x in num_list1]
        p_list = [x for x in p_list1]
        for p in P: #[+,*,-]
            while p in p_list:
                p_index = p_list.index(p)
                p_list.pop(p_index)
                n1 = num_list.pop(p_index + 1)
                if p == "+":
                    num_list[p_index] = num_list[p_index] + n1
                elif p == '-':
                    num_list[p_index] = num_list[p_index] - n1
                elif p == '*':
                    num_list[p_index] = num_list[p_index] * n1

        return num_list[0]

    num = ""
    p_ = ["+", "-", "*"]
    p_list = []
    num_list =[]
    p_sort = [["+", "-", "*"], ["+", "*", "-"], ["-","+", "*"], ["-","*","+"], ["*", "+", "-"], ["*","-", "+"]]
    for x in expression:
        if x not in p_:
            num += x
        else:
            num_list.append(int(num))
            num = ""
            p_list.append(x)
    num_list.append(int(num))
    for P in p_sort:
        answer = max(abs(answer), abs(cal(P, num_list, p_list)))


    return answer

print(solution("100-200*300-500+20"))