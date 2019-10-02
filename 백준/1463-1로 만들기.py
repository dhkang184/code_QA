from copy import copy as copy

n = int(input())
results = []
results.append(n)
time = 0



while (min(results) != 1):
    #temps = [x for x in set(results)]
    temps = results
    time += 1
    results =[]
    for i in temps:
        results.append(i-1)
        if i%3 == 0:
            cal_all = i//3
            results.append(cal_all)
        elif i%2 ==0:
            cal_all = i//2
            results.append(cal_all)
    set(results)

print(time)

"""
save = {1:0, 2:1}
def frog(n):
    if n in save:
        return save[n]
    m = 1+min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))
"""