# #https://www.acmicpc.net/problem/1439
# # 22:48~ 23:27
#
# S = input()
#
# zero_check =[0] * len(S)
# one_check =[1]* len(S)
#
# list_S = []
# for x in S:
#     list_S.append(int(x))
#
# from collections import deque
#
# que = deque()
# que.append((0,list_S))
# while True:
#     step, C_list = que.popleft()
#     if sum(C_list) ==0 or sum(C_list) == len(S):
#         print(step)
#         break
#     switch_num = C_list[0]
#     start_idx =0
#     end_idx =0
#     for idx, v in enumerate(C_list):
#         if v != switch_num or idx == len(C_list) -1:
#             end_idx = idx
#             if switch_num ==0:
#                 switch_num =1
#                 N_list = []
#                 for idx2 in range(len(C_list)):
#                     if idx2 >=start_idx and idx2 < end_idx:
#                         N_list.append(switch_num)
#                     else:
#                         N_list.append(C_list[idx2])
#             elif switch_num ==1:
#                 switch_num =0
#                 N_list = []
#                 for idx2 in range(len(C_list)):
#                     if idx2 >=start_idx and idx2 < end_idx:
#                         N_list.append(switch_num)
#                     else:
#                         N_list.append(C_list[idx2])
#             que.append((step+1, N_list))
#
#             start_idx =idx


data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
