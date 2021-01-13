def solution(N):
    m_list = [500,100,50,10]
    money = N
    cnt = 0
    for x_idx, x in enumerate(m_list):
        cnt += N//x # //: 정수로 나누기, /: 유리수로 나눔
        N %= x
    print(cnt)


    return cnt

solution(600)