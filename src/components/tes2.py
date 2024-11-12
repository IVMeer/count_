def bubble(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

num = [2,5,1,3,4]
print("bubbleSort:",bubble(num))

def selectionSort(num):
    for i in range(len(num)):
        min = i
        for j in range(i+1, len(num)):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]
    return num

num = [2,5,1,3,4]
print("selectionSort:", selectionSort(num))


def insertSort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i-1
        while j >= 0 and key <num[j]:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = key
    return num

num = [2,5,1,3,4]
print("insertSort:",insertSort(num))
