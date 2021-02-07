#page 312

def solution():
    N = input()
    result =0
    for x in N:
        if int(x) >1 and result >0:
            result *= int(x)
        else:
            result += int(x)
    print(result)

solution()