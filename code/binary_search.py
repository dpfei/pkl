# -*- coding: utf-8 -*-
def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if data_list[mid] == target:
            return data_list[mid], mid
        elif data_list[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return target, -1

data_list = [element for element in range(1,101)]
print(data_list)
target, index = binary_search(data_list, 11)
print("目标值 %s，目标值位置 %s" %(target, index))


