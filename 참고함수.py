#순열 조합 , :https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

#1. 순열
def permutation1(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    global AAA
    AAA = []

    def generate(chosen, used):
        # 2.

        if len(chosen) == r:
            print(chosen)
            AAA.append(chosen)
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return AAA

#중복 해결
def permutation(arr, r):
    # 1.
    arr = [1,3,2]
    r = 3
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    global result
    result = []
    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            result.append([x for x in chosen])
            return

        for i in range(len(arr)):
            # 3.
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([],used)

    return result

#permutation([1, 2, 3, 4, 5], 3)

#2. 조합
def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

# 중복해결
def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

import itertools
mylist = [1,2,3]
result = itertools.combinations(mylist, r=2)
result = itertools.combinations_with_replacement(mylist, r=2)



from collections import deque
que = deque(['bb','cc'])
que.append('aaa')
que.popleft()
