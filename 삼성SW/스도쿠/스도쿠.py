for T in range(int(input())) :
    Check_row = [[0 for i in range(9)] for j in range(9)]
    Check_col = [[0 for i in range(9)] for j in range(9)]
    Check_squ = [[[0 for k in range(9)] for i in range(3)] for j in range(3)]
    F = 1
    for i in range(9) :
        row = list( map( int, input().split(sep=' ')) )
        if F :
            for j in range(9) :
                num = row[j]
                if [Check_row[i][num-1], Check_col[j][num-1], Check_squ[int(i//3)][int(j//3)][num-1] ] == [0,0,0] :
                    [Check_row[i][num-1], Check_col[j][num-1], Check_squ[int(i//3)][int(j//3)][num-1] ] = [1,1,1]
                else :
                    F = 0
                    break
    print('#{} {}'.format(T+1, F) )