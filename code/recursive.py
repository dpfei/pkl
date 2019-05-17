# _*_ coding: utf-8 _*_
import time

# 递归统计列表包含的元素数
def element_total(data_list):
    pass

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
    time.sleep(1)
    countdown(i-1)

print(element_total([1,2,3]))