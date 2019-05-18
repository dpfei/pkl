# _*_ coding: utf-8 _*_
from time import sleep
import random

# 递归查找列表中最大的元素
def findMaxElement(data_list):
    max_num = data_list.pop(0)
    if data_list!= []:
        find_num = findMaxElement(data_list=data_list)
        if find_num > max_num:
            max_num = find_num
    return max_num

# 递归统计列表包含的元素数
def element_total(arr):
    total = 0
    if arr != []:
        arr.pop(0)
        total = 1 + element_total(arr)
    return total

# 对一个一维数字数组进行递归求和
def sum(arr):
    total = 0
    if len(arr) > 1:
        total = arr.pop(0) + sum(arr)
    else:
        total = arr[0]
    return total

# 阶乘递归函数
def factorial(n):
    res = 1
    if n == 1:
        return res
    else:
        res = n * factorial(n-1)
    return res

# 递减递归函数
def countdown(i):
    print(i)
    if i < 0:
        return None
    sleep(1)
    countdown(i-1)


sort_list = list(range(100))
random.shuffle(sort_list)
print(findMaxElement(sort_list))