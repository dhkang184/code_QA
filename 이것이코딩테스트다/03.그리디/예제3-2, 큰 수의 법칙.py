#N,M,K 공백으로 구분하여 입력

def solution():
    n,m,k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    f_idx = data[-1]
    s_idx = data[-2]
    cnt = int(m/(k+1))*k
    cnt += m%(k+1)

    result = f_idx*cnt + s_idx*(m-cnt)
    print(result)

