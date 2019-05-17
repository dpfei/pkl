# _*_ coding: utf-8 _*_
import random
def findSmallest(data_list):
    # 查找列表中最小元素
    smallest = data_list[0]
    smallest_index = 0
    for i in range(1, len(data_list)):
        if data_list[i] < smallest:
            smallest = data_list[i]
            smallest_index = i
    return smallest_index

def selectionSort(data_list):
    new_list = list()
    for i in range(len(data_list)):
        smallest_index = findSmallest(data_list=data_list)
        new_list.append(data_list.pop(smallest_index))
    return new_list

blist = list(range(100))
random.shuffle(blist)
print('排序前列表======>', blist)
print('排序后列表======>', selectionSort(blist))
        
