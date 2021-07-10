#https://www.hackerrank.com/challenges/the-minion-game/problem
# 23:15~

def minion_game(S):
    Stuart = 0
    Kevin =0

    for idx , c in enumerate(S):
        if c in 'AEIOUWY':
            Kevin += len(S) -idx
        else:
            Stuart += len(S) -idx
    if Stuart >= Kevin:
        print('Stuart %d' %Stuart)
    else:
        print('Kevin %d' %Kevin)