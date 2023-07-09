nums_list = [10,23,45,70,11,15]
target = 70

def func(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 'found'
    return '-1'

func(nums_list, target)