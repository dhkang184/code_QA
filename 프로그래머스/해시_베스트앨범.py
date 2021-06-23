#https://programmers.co.kr/learn/courses/30/lessons/42579
# 23:40~ 24:20

def solution(genres, plays):
    answer = []
    ans_list = [x for x in range(len(genres))]
    genr_list = list(set(genres))
    genr_dict = dict(zip(genr_list,[[] for _ in range(len(genr_list))]))
    genr_count = [0] * len(genr_list)
    G_dict = dict(zip(genr_list,genr_count))
    map_list = list(zip(ans_list, genres, plays))
    for x in map_list:
        x_idx, genr, play = x
        G_dict[genr] += play
        G_list = genr_dict[genr]
        G_list.append((play, x_idx))
        genr_dict[genr] = G_list

    sorted_genres = sorted(G_dict.items(), key=lambda x: -x[1] )

    for G_value in sorted_genres:
        P_list = sorted(genr_dict[G_value[0]], key=lambda x: (x[0], -x[1]), reverse=True)
        for P_value in P_list[:2]:
            answer.append(P_value[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600,
                                                                150, 800, 2500]))