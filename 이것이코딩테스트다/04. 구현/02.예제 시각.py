#page 113
def solution1():
    N = int(input())
    c = 0
    for min in range(60):
        for sec in range(60):
            if '3' in str(min) or '3' in str(sec):
                c +=1
    time = [c] *24
    time[3],time[13], time[23] = 3600, 3600, 3600
    print(sum(time[:N+1]))

def solution2():
    h = int(input())
    cnt = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    cnt += 1
    print(cnt)
solution1()