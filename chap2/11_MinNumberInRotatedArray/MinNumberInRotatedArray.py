

#函数功能：找出旋转数组的最小数字
#思路一 解题思路：遍历数组,找出数组的最小值
#算法复杂度:O(N)

def MinNumberInRotatedArray_way1(array):
    if array==None or len(array)==0:   #判断数组是否为空数组
        return None
    minValue=array[0]                  #初始化数组的最小值
    for index in range(1,len(array)):
        if array[index]<minValue:
            minValue=array[index]
    return minValue

#函数功能：找出旋转数组的最小数字
#思路二 解题思路：二分查找
#算法复杂度:O(log N)

def MinNumberInRotatedArray_way2(array):
    if array==None or len(array)==0:    #判断数组是否为空数组
        return None
    leftIndex=0                               #初始化搜索区间的左右边界下标
    rightIndex=len(array)-1
    midIndex=0                                #初始化搜索区间的中间下标

    if array[leftIndex]<array[rightIndex]:    #此时数组并未被旋转，第一个元素就是最小元素
        return array[0]

    while array[leftIndex]>=array[rightIndex]:
        if rightIndex-leftIndex==1:           #当两个移动下标索引相邻时，跳出循环
            midIndex=rightIndex
            break
        midIndex=(rightIndex+leftIndex)//2    #更新搜索区间的中间元素的下标

        #如果左右边界、中间点三者数值相等
        # 此时只能判断最小值在这段搜索区间内，但是无法再进行二分查找了
        if array[leftIndex]==array[midIndex] and array[midIndex]==array[rightIndex]:
            return  minSearch(array,leftIndex,rightIndex)

        # 如果该中间元素位于前面的递增子数组，那么它应该大于或者等于第一个指针指向的元素
        if array[midIndex]>=array[leftIndex]:
            leftIndex=midIndex

        #如果中间元素位于后面的递增子数组，那么它应该小于或者等于第二个指针指 向的元素
        elif array[midIndex]<=array[rightIndex]:
            rightIndex=midIndex
    return array[midIndex]

#函数功能：针对思路二中无法再进行二分查找的搜索区间，进行顺序查找
def minSearch(array,index1,index2):
    minValue=array[index1]
    for index in range(index1,index2+1):
        if array[index]<minValue:
            minValue=array[index]
    return minValue

if __name__=="__main__":
    array=[3,4,5,1,2]
    print(MinNumberInRotatedArray_way1(array))
    print(MinNumberInRotatedArray_way2(array))

    array=[1,0,1,1,1]
    print(MinNumberInRotatedArray_way1(array))
    print(MinNumberInRotatedArray_way2(array))
