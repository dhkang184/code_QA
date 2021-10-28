def letterCombinations(digits):
    p_dict = {'2': 'abc',
              '3': 'def',
              '4': 'ghi',
              '5': 'jkl',
              '6': 'mno',
              '7': 'pqrs',
              '8': 'tuv',
              '9': 'wxyz',
              '0': ' '}

    visited = [0] * len(digits)

    ans = []

    def dfs(digits, p_dict, v_idx, s):
        if v_idx == len(digits):
            ans.append(s)
            return 0

        for k in p_dict[digits[v_idx]]:
            dfs(digits, p_dict, v_idx + 1, s + k)

    dfs(digits, p_dict, 0, "")
    return ans

print(letterCombinations('23'))