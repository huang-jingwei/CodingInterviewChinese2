# 面试题40：最小的k个数

**题目：**  输入n个整数，找出其中最小的k个数。



**例如：** 输入4、5、1、6、2、7、3、8。则最小的4个数字是1、2、3、4。



牛客网OJ：[最小的K个数](https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)



**思路一：**  先将输入n个整数进行排序，排序排序之后最前面的k个数就是最小的k个数

快速排序算法的时间复杂度：O(N)

**思路二：**  基于partition函数

可以基于partition函数来解决这个问题。如果基于数组的第k个数字来调整，则使得比第k个数字小的所有数组都位于数组的左边，比第k个数字大的所有数组都位于数组的右边。这样调整后，位于数组中左边的k个数字就是最小的k个数字（注意：这k个数字不一定是排序的）



