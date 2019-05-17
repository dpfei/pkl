# _*_ coding: utf-8 _*_
import random

# 冒泡排序，数值大的元素在前，降序排序
def bubble_sort(data_list):
    data_len = len(data_list)
    for i in range(data_len-1):
        for j in range(data_len-1-i):
            if data_list[j] < data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list

blist = list(range(100))
random.shuffle(blist)
print('无序列表======>', blist)
res_list = bubble_sort(data_list=blist)
print('有序列表======>', res_list)