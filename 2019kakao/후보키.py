# # https://www.welcomekakao.com/learn/courses/30/lessons/42890
#
# from itertools import combinations
#
# def remove_list(total_list, accepted_key):
#     new_list =[]
#     for par in total_list:
#         check_key = ""
#         for x in par:
#             check_key += str(x)
#         check_idx = 0
#         for y in accepted_key:
#             if y in check_key:
#                 check_idx = 1
#                 break
#         if check_idx == 0:
#             new_list.append(check_key)
#
#     return new_list
#
# def new_list(removed_list, col_dict, total_row):
#     check_dict = {}
#     new_key = []
#     for keys in removed_list:
#         for row_idx in range(total_row):
#             new_val = ""
#             for val_key in keys:
#                 new_val += col_dict[val_key][row_idx]
#
#             if keys not in check_dict:
#                 check_dict[keys] =[new_val]
#             else:
#                 check_dict[keys].append(new_val)
#
#         if total_row == len(set(list(check_dict[keys]))):
#             new_key += [keys]
#     return new_key
#
#
# def solution(relation):
#     answer = 0
#     accept_key = []
#     total_row = len(relation)
#     total_col = len(relation[0])
#     keys = [str(x) for x in range(total_col)]
#
#     col_dict = {}
#     #### make 1 col dict
#     for rows in relation:
#         for col in range(total_col):
#             if keys[col] not in col_dict:
#                 col_dict[keys[col]] =[rows[col]]
#             else:
#                 col_dict[keys[col]].append(rows[col])
#     for key_idx in keys:
#         if total_row == len(set(list(col_dict[key_idx]))):
#             accept_key.append(key_idx)
#
#     for x in range(total_col-2):
#         new_key = list(combinations(keys, x+2))
#         removed_list = remove_list(new_key, accept_key)
#         accept_key += new_list(removed_list,col_dict,total_row)
#
#     answer = len(accept_key)
#
#
#     return answer


from itertools import combinations
def solution(relation):
    answer = 0
    relation = [['100', 'ryan', 'music', '2'], ['200', 'apeach', 'math', '2'], ['300', 'tube', 'computer', '3'],
                ['400', 'con', 'computer', '4'], ['500', 'muzi', 'music', '3'], ['600', 'apeach', 'music', '2']]
    accept_key = []
    total_row = len(relation)
    total_col = len(relation[0])
    col_list = [ x for x in range(total_col)]
    key_list = []
    for col in range(total_col):
        key_list.append([list(x) for x in list(combinations(col_list, col+1))])
    col_dict = {}
    #### make 1 col dict
    for rows in relation:
        for col in range(total_col):
            if key_list[0][col][0] not in col_dict:
                col_dict[key_list[0][col][0]] =[rows[col]]
            else:
                col_dict[key_list[0][col][0]].append(rows[col])

    for idx in range(total_col):
        if len(set(list(col_dict[idx]))) == total_row:
            accept_key.append(key_list[0][idx])

    for key_list_idx in range(len(key_list)):
        for key_idx in range(len(key_list[key_list_idx])):

            accept_check = 0
            for ac_key in accept_key:
                #accept = ''.join(str(ac_key))
                #check_key = ''.join(str(key_list[key_list_idx][key_idx]))
                accept =""
                check_key =""
                for ac in ac_key:
                    accept += str(ac)
                for ch in key_list[key_list_idx][key_idx]:
                    check_key +=str(ch)
                if accept in check_key:
                    accept_check = 1
                    break
            if accept_check == 0:

                check_list = []
                for rows in range(total_row):
                    new_val = ""
                    for cols in key_list[key_list_idx][key_idx]:
                        new_val += col_dict[cols][rows]
                    check_list.append(new_val)
                if len(set(list(check_list))) == total_row:
                    accept_key.append(key_list[key_list_idx][key_idx])
    answer= len(accept_key)
    print(answer)
    return answer
relation = [['100', 'ryan', 'music', '2'], ['200', 'apeach', 'math', '2'], ['300', 'tube', 'computer', '3'], ['400', 'con', 'computer', '4'], ['500', 'muzi', 'music', '3'], ['600', 'apeach', 'music', '2']]

solution(relation)