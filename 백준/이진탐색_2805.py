#https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())

t_list = list(map(int, input().split()))

def binary(mid , t_list):
    cut =0
    for t in t_list:
        if t > mid:
            cut += t-mid
    return cut

start = 0
end = max(t_list)
answer = end
while start <=end:
    mid = (start + end) //2
    C = binary(mid, t_list)
    if C>= m:
        answer = mid
        start = mid +1
    else:
        end = mid -1

print(answer)