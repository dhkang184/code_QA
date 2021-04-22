#https://programmers.co.kr/learn/courses/30/lessons/42626
# 시작시간: 17:40 ~ 18:10

# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     if K <= scoville[0]:
#         return answer
#
#     while True:
#         if len(scoville) <2:
#             return -1
#         answer +=1
#         n_value = scoville[0] + (scoville[1] *2)
#         scoville =[n_value] + scoville[2:]
#         scoville.sort()
#         if scoville[0] >= K:
#             return answer

import heapq

def solution(scoville, k):
  heap = []
  for num in scoville:
      heapq.heappush(heap, num)

  mix_cnt = 0
  while heap[0] < k:
      try:
          heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
      except IndexError:
          return -1
      mix_cnt += 1

  return mix_cnt
