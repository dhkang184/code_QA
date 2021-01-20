#quick sort

arrray = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left +=1
        while right <= end and array[right] >= arrray[pivot]:
            right -= 1

        if left > right:
            arrray[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right],array[left]
    quick_sort(array,start, right-1)
    quick_sort(array,right+1,end)

quick_sort(arrray, 0 , len(arrray) -1)

def py_quick_sort(array):
    if len(array) <=1:
        return array

    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return py_quick_sort(left_side) + [pivot] + py_quick_sort(right_side)