# _*_ coding:utf-8 _*_

def mergeSort(arr):
    # 归并排序
    # 参考资料：https://www.cnblogs.com/chengxiao/p/6194356.html
    if len(arr) >= 2:
        mid = int(len(arr)/2)
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        # 对每次递归进行排序合并并返回排序结果
        # int为舍去取整
        i = 0
        j = 0
        temp = list()
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        while i < len(left):
            temp.append(left[i])
            i += 1
        while j < len(right):
            temp.append(right[j])
            j += 1
        return temp
    else:
        return arr

print(mergeSort([1,2,3,8,5,9,12,50,33]))

