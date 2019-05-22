# _*_ coding: utf-8 _*_

# 杨辉三角
# 参考资料：https://www.cnblogs.com/clover-toeic/p/3766001.html
# TODO 对代码进行优化

def pascal_triangle(max_row):
    res = []
    for i in range(max_row):
        res.append([])
        for j in range(max_row):
            res[i].append(0)
    for i in range(max_row):
        res[i][0] = 1
        res[i][i] = 1
    for i in range(2,max_row):
        for j in range(1,i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    for i in range(max_row):
        for j in range(i+1):
            print(res[i][j])
        print('\n')
    


pascal_triangle(5)