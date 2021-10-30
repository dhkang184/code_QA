#https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

def man_dis(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

def check_p(place):
    persons = []
    for r in range(len(place)):
        for c in range(len(place[0])):
            if place[r][c] == 'P':
                persons.append((r,c))
    for p_idx in range(len(persons)):
        for check_p in range(p_idx+1, len(persons)):
            r1 = persons[p_idx][0]
            c1 = persons[p_idx][1]
            r2 = persons[check_p][0]
            c2 = persons[check_p][1]
            if abs(r1- r2) + abs(c1-c2) <=2:
                if r1 == r2:
                    pass_v = True
                    for n_c in range(min(c1,c2), max(c1,c2)):
                        if place[r1][n_c] == 'X':
                            pass_v = False
                    if pass_v:
                        return 0
                elif c1 == c2:
                    pass_v = True
                    for n_r in range(min(r1,r2), max(r1,r2)):
                        if place[n_r][c1] == 'X':
                            pass_v =False
                    if pass_v:
                        return 0
                else:
                    delta_r = r2- r1
                    delta_c = c2 -c1
                    if place[r1][c2] == 'O' or place[r2][c1] =='O':
                        return 0
    return 1



def solution(places):
    answer = []
    for place in places:
        answer.append(check_p(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
