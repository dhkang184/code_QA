#https://programmers.co.kr/learn/courses/30/lessons/43163
#22:25~ 22:55

def solution(begin, target, words):
    from collections import deque
    answer = 0
    visited = [False] * len(words)
    q = deque([begin])
    step = 0
    if target not in words:
        return 0

    while q:
        q_len = len(q)
        for i in range(q_len):
            val = q.popleft()
            if val == target:
                return step
            for j in range(len(words)):
                if visited[j] == False:
                    compare_word = words[j]
                    sub_num =0
                    if val == compare_word:
                        visited[j] = True
                    else:
                        for val_w, compare_w in zip(val, compare_word):
                            if val_w != compare_w:
                                sub_num +=1
                        if sub_num ==1:
                            visited[j] = True
                            q.append(compare_word)
        step += 1
    return answer

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))