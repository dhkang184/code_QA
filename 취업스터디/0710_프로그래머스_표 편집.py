#https://programmers.co.kr/learn/courses/30/lessons/81303
# 13:15~
# from collections import deque
# def solution(n, k, cmd):
#     del_list = []
#     answer = ''
#     ans_list = ['O']*n
#     c_list = [i for i in range(n)]
#     for c in cmd:
#         if c =="C":
#             if k == len(c_list) -1:
#                 del_idx = c_list.pop()
#                 del_list.append((del_idx,k))
#                 ans_list[del_idx] = 'X'
#                 k -=1
#             else:
#                 del_idx = c_list.pop(k)
#                 del_list.append((del_idx,k))
#                 ans_list[del_idx] = 'X'
#         elif c == "Z":
#             add_v, add_idx = del_list.pop()
#             ans_list[add_v] = 'O'
#             c_list.insert(add_idx, add_v)
#             if add_idx <= k:
#                 k +=1
#
#         elif c[0] =='D':
#             D, N = c.split()
#             k += int(N)
#         elif c[0] == 'U':
#             U, N = c.split()
#             k -= int(N)
#
#     answer = ''.join(ans_list)
#
#     return answer

def solution(n, k, cmd):
    del_list = []
    answer = ''
    ans_list = ['O']*n

    for c in cmd:
        if c =="C":
            ans_list[k] = 'X'
            del_list.append(k)
            end_v = True
            for n_k in range(k, n):
                if ans_list[n_k] == 'O':
                    k = n_k
                    end_v = False
                    break

            if end_v:
                for n_k in range(k, -1, -1):
                    if ans_list[n_k] == 'O':
                        k = n_k
                        end_v = False
                        break
        elif c == "Z":
            z_v = del_list.pop()
            ans_list[z_v] = 'O'

        elif c[0] =='D':
            D, N = c.split()
            # new_del_list = sorted(del_list)
            N = int(N)
            # for c_idx in new_del_list:
            #     if k<= c_idx <=k + N:
            #         N +=1
            #     elif c_idx > k+N:
            #         break
            # k = k+N

            for c_idx in range(k, n):
                if ans_list[c_idx] == 'X':
                    N +=1
                if c_idx >= k + N and ans_list[c_idx] =='O':
                    k = c_idx
                    break

        elif c[0] == 'U':
            U, N = c.split()
            N = int(N)
            # new_del_list = sorted(del_list, reverse=True)
            # N = int(N)
            # for c_idx in new_del_list:
            #     if k-N<= c_idx <=k:
            #         N +=1
            #     elif c_idx < k-N:
            #         break
            # k = k-N


            for c_idx in range(k, -1, -1):
                if ans_list[c_idx] == 'X':
                    N +=1
                if c_idx <= k - N and ans_list[c_idx] =='O':
                    k = c_idx
                    break

    answer = ''.join(ans_list)
    return answer


print(solution(8,2 ,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))