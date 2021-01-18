#page 110
def solution():
    n = int(input())
    move =  input().split()
    move_key = ["L","R","U","D"]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    x,y = 1,1

    for m in move:
        for k_idx, k in enumerate(move_key):
            if k == m:
                nx = x+ dx[k_idx]
                ny = y+ dy[k_idx]
                break
        if nx <1 or ny <1 or nx >n or ny >n:
            continue
        x, y = nx,ny
    print(x,y)

solution()