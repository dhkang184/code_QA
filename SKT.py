def solution(T):
    s = "1234"
    print(s[0])

    print(len(s))

    l = len(s)
    cur = int((l) / 2)
    if (s[0] != s[l - 1]):
        print(0)
    l_cur = 0
    r_cur = l - 1
    while (cur > 0 and l_cur != r_cur):
        if (s[0:cur] == s[l - cur:l]):
            l_cur = cur
            cur = int((cur + r_cur) / 2)
            print("l_cur: %d\n", l_cur, r_cur, cur)
        else:
            r_cur = cur
            cur = int((cur + l_cur) / 2)
            print("r_cur: %d\n", l_cur, r_cur, cur)

    print(cur)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution3(S):
    # write your code in Python 3.6
    lines = S.split('\n')
    value_dict = {}
    for x_idx, x in enumerate(lines):
        pic_name, pic_city, pic_date = x.split(', ')
        pic_type = pic_name.split('.')[-1]
        if pic_city not in value_dict:
            value_dict[pic_city] = []

        if pic_type != 'jpg' and pic_type != 'png' and pic_type != 'jpeg':
            continue

        copy_list = value_dict[pic_city]
        copy_list.append([pic_date, x_idx, pic_type])
        value_dict[pic_city] = copy_list

    ### city list change
    answer_list = [0] * len(lines)
    for key_city in value_dict.keys():
        num_city = len(value_dict[key_city])
        sorted_city = sorted(value_dict[key_city])
        zfill_size = len(str(num_city))

        for i in range(1, num_city + 1):
            answer_idx = sorted_city[i - 1][1]
            pic_type = sorted_city[i - 1][2]
            answer_list[answer_idx] = key_city + str(i).zfill(zfill_size) + '.' + pic_type

    return '\n'.join(answer_list)


S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22'

#solution3(S)

"""
def solution4(S):
    n = len(S)
    L_pre = [0] * n
    l = 0
    i = 1
    while (i < n):
        if (S[i] == S[l]):
            l = l + 1
            L_pre[i] = l
            i = i + 1
        else:
            if (l != 0):
                l = L_pre[l - 1]
            else:
                L_pre[i] = 0
                i = i + 1

    answer = L_pre[n - 1]

    return answer
"""

def solution4(S):
    L_pre = [0] * len(S)
    left_idx = 0
    i = 1
    while (i < len(S)):
        if (S[i] == S[left_idx]):
            left_idx = left_idx + 1
            L_pre[i] = left_idx
            i = i + 1
        elif left_idx ==0:
            L_pre[i] = 0
            i = i + 1
        else:
            left_idx = L_pre[left_idx - 1]

    answer = L_pre[len(S) - 1]

    return answer


print(solution4('aaabbaaa'))