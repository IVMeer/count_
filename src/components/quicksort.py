def quick_sort(arr):
    if len(arr) <= 1:
        print("arr:",arr)
        return arr
    else:
        pivot = arr[len(arr) // 2]
        print("pivot:",pivot)
        left = [x for x in arr if x < pivot]
        print("left:",left)
        middle = [x for x in arr if x == pivot]
        print("middle:",middle)
        right = [x for x in arr if x > pivot]
        print("right:",right)
        print('-----------------------')
        return quick_sort(left) + middle + quick_sort(right)

# 示例用法
numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
