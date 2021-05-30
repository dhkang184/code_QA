#01:00

def solution(H):
    h_list = []
    count = 0
    for x in H:
        if len(h_list) ==0:
            h_list.append(x)
            count +=1
        else:
            while True:
                if len(h_list) == 0:
                    h_list.append(x)
                    count += 1
                    break

                if h_list[-1] < x:
                    h_list.append(x)
                    count += 1
                    break
                elif h_list[-1] == x:
                    break
                else:
                    h_list.pop()

    return count

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))