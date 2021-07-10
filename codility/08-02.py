#23:15~

def solution(A):
    # write your code in Python 3.6

    right_map = dict()
    for data in A:
        if data in right_map:
            right_map[data] = right_map[data] + 1
        else:
            right_map[data] = 1

    left_leader = 0
    left_leader_count = 0
    left_map = dict()
    # size of length
    right_length = len(A)
    left_length = 0
    result_count = 0
    for data in A:
        # decrease 1 from right_map
        right_map[data] = right_map[data] - 1
        right_length -= 1

        # add 1 to left_map
        if data in left_map:
            left_map[data] = left_map[data] + 1
        else:
            left_map[data] = 1
        left_length += 1

        # get left leader
        if left_map[data] > left_leader_count:
            left_leader = data
            left_leader_count = left_map[data]

        # check left leader equals right leader
        if left_leader_count > left_length // 2 and right_map[left_leader] > right_length // 2:
            result_count += 1

    return result_count