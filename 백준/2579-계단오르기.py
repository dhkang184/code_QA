max_T = int(input())

#one2_step = {} #이전에 연속으로 한칸 올라옴
one_step = {0:0}
two_step = {0:0} # 이전에 두칸 올라옴

for idx in range(1,max_T+1):
    cur_state = int(input())
    if idx == 1:
        one_step[idx] = cur_state
    if idx == 2:
        one_step[idx] = one_step[idx-1] + cur_state
        two_step[idx] = cur_state
    if idx == 3:
        one_step[idx] = two_step[idx-1] + cur_state
        two_step[idx] = one_step[idx-2] + cur_state
    # if idx ==4:
    #     one_step[idx] = two_step[idx - 1] + cur_state
    #     two_step[idx] = two_step[idx - 2] + cur_state
    if idx > 3:
        one_step[idx] = two_step[idx-1] + cur_state
        two_step[idx] = max(one_step[idx-2], two_step[idx-2]) + cur_state

print(max(one_step[idx], two_step[idx]))