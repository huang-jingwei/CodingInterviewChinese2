import  numpy as np
import random

#函数功能：判断二维数组中是否含有该整数k
#解题思路：将该问题转化成求解数组中位数的问题
#算法复杂度:O(N+M)

def FindInPartiallySortedMatrix(array,k):
    if array.shape[0]==0 or array.shape[1]==0: #判断数组是否为空数组
        return None
    rowIndex=0                           #初始化移动下标,从数组的右上角开始寻找
    colIndex=array.shape[1]-1
    while rowIndex<=array.shape[0]-1 and colIndex>=0:
        if array[rowIndex,colIndex]==k:  #当前元素数值等于整数k
            return True
        elif array[rowIndex,colIndex]>k: #当前元素数较大时，该矩阵为递增矩阵，列位置减1，移动到较小的元素
            colIndex=colIndex-1
        elif array[rowIndex,colIndex]<k: #当前元素数较小时，该矩阵为递增矩阵，行位置加1，移动到较大的元素
            rowIndex=rowIndex+1
    return False

if __name__=="__main__":
    array=np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13]])
    print(FindInPartiallySortedMatrix(array, k=13))

    array = np.array([[0, 1, 2, 3, 4, 5, 6],
                      [10, 12, 13, 15, 16, 17, 18],
                      [23, 24, 25, 26, 27, 28, 29],
                      [44, 45, 46, 47, 48, 49, 50],
                      [65, 66, 67, 68, 69, 70, 71],
                      [96, 97, 98, 99, 100, 111, 122],
                      [166, 176, 186, 187, 190, 195, 200],
                      [233, 243, 321, 341, 356, 370, 380]])
    print(FindInPartiallySortedMatrix(array,k=500))


