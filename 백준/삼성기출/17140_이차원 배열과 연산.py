#https://www.acmicpc.net/problem/17140
#  00:00~ 1:05

r,c,k = map(int, input().split())

A = [list(map(int, input().split())) for x in range(3)]

def _R(A):
    n_A = []
    for idx, x in enumerate(A):
        line_dict = {}
        for x_value in x:
            if x_value not in line_dict and x_value != 0:
                line_dict[x_value] =(x_value,1)
            elif x_value != 0:
                line_dict[x_value] = (x_value, line_dict[x_value][1] +1)
        new_line = [line_dict[key] for key in line_dict.keys()]
        new_line = sorted(new_line, key = lambda x: (x[1], x[0]))
        n_line = []
        for n_list in new_line:
            n_line.append(n_list[0])
            n_line.append(n_list[1])
        n_A.append(n_line)

    max_len =0
    for y in range(len(n_A)):
        max_len = max(max_len, len(n_A[y]))

    for z in range(len(n_A)):
        n_A[z] = n_A[z] +[0] *(max_len - len(n_A[z]))

    return n_A

def _C(A):
    n_A = []
    for x_idx in range(len(A[0])):
        line_dict = {}
        for y_idx in range(len(A)):
            y_value = A[y_idx][x_idx]
            if y_value not in line_dict and y_value != 0:
                line_dict[y_value] = (y_value, 1)
            elif y_value != 0:
                line_dict[y_value] = (y_value, line_dict[y_value][1] + 1)
        new_line = [line_dict[key] for key in line_dict.keys()]
        new_line = sorted(new_line, key=lambda x: (x[1], x[0]))
        n_line = []
        for n_list in new_line:
            n_line.append(n_list[0])
            n_line.append(n_list[1])
        n_A.append(n_line)

    max_len = 0
    for y in range(len(n_A)):
        max_len = max(max_len, len(n_A[y]))

    new_A = [[0]*len(A[0]) for _ in range(max_len)]

    for y in range(len(n_A)):
        for x in range(len(n_A[y])):
            new_A[x][y] = n_A[y][x]
    return new_A

answer = -1
for x in range(101):
    try:
        if A[r-1][c-1] ==k:
            answer = x
            break
    except:
        pass
    if len(A) >= len(A[0]):
        A = _R(A)
    else:
        A = _C(A)

print(answer)