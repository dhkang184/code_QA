#기본 이진탐색

def binary_search(array, target, start, end):
    # 재귀함수로 이진탐색 함수
    if start> end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start, mid -1)
    else:
        return binary_search(array,target, mid+1, end)

def binary_search2(array,target, start, end):
    while start <= end:
        mid = (start+ end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

# 빠르게 입력 받기
def fast_input():
    import sys
    input_data = sys.stdin.readline().rstrip()


