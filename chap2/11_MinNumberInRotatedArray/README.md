# 面试题11：旋转数组的最小数字



【题目】把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减序列的一个旋转，输出旋转数组的最小元素。



【例如】数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。



牛客网OJ：[旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-rankingg)



**思路一：遍历实现**

算法时间复杂度：O（N）

```python
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
```



**思路二：二分查找**

【分析】我们注意到旋转之后的数组实际上可以划分为两个排序的子数组，而且 **前面的子数组的元素都大于或者等于后面子数组的元素。我们还可以注意到最小的元素刚好是这两个子数组的分界线。**

算法时间复杂度：O（log N）





首先我们用两个指针，分别指向数组的第一个元素和最后一个元素。按照题目旋转的规则，第一个元素应该是大于或者等于最后一个元素的（这其实不完全对，还有特例。后面再讨论特例）。

接着我们得到处在**数组中间的元素**

- 如果该中间元素位于前面的递增子数组，那么它应该大于或者等于第一个指针指向的元素。

此时数组中最小的元素应该位于该中间 元素的后面。我们可以把第一指针指向该中间元素，这样可以缩小寻找的范围。

- 同样，如果中间元素位于后面的递增子数组，那么它应该小于或者等于第二个指针指 向的元素。此时该数组中最小的元素应该位于该中间元素的前面。我们可以把第二个指针指向该中间元素，这样同样可以缩小寻找的范围。我们接着再用更新之后的 两个指针，去得到和比较新的中间元素，循环下去。



按照上述的思路， **我们的第一个指针总是指向前面递增数组的元素，而第二个指针总是指向后面递增数组的元素。** 最后第一个指针将指向前面子数组的最后一个元素， 而第二个指针会指向后面子数组的第一个元素。也就是它们最终会指向两个相邻的元素，而第二个指针指向的刚好是最小的元素。这就是循环结束的条件。





我们考虑下特殊情况，我们的循环判断是以`rotateArray[low] >= rotateArray[high]`为条件的，不满足这个的特殊情况有那些呢？

由于是把递增排序数组前面的若干个数据搬到后面去，因此第一个数字总是大于或者等于最后一个数字，但按照定义还有一个



**特殊情形一：数组并未被旋转**

**开始时就rotateArray[low] < rotateArray[high]，那么循环不会执行**

- 如果数组旋转后仍然有序，即rotateArray[low] < rotateArray[high]

> 如果把排序数组前面0个元素搬到后面，也就是说其实没有旋转，

> 

> 那么第0个元素就是最小的元素

> 

> 因此我们将mid初始化为0



现在可以了么，有没有特殊情况仍然未被处理的，

如果rotateArray[low] = rotateArray[high]

> 测试用例: [1, 0, 1, 1, 1, 1]
>
> 对应输出应该为:
>
> 0
>
> 你的输出为:
>
> 1

此时

> rotateArray[low] ,rotateArray[mid] ,rotateArray[high]三者相等

> 无法确定中间元素是属于前面还是后面的递增子数组

> 只能顺序查找





```python
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
```












