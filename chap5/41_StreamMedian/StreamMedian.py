import random

################大根堆模块：建立大根堆、调整大根堆################
#建立大根堆
def bigHeapInsert(array,index):
    parentIndex=(index-1)//2       #父节点的下标索引
    while parentIndex>=0 and array[parentIndex]<array[index]:
        array[index],array[parentIndex]=array[parentIndex],array[index]
        index=parentIndex          #交换后，更新节点信息
        parentIndex = (index - 1) // 2

#调整大根堆
def bigHeapeapIfy(array,index):
    leftSonIndex=2*index+1                          #左右儿子节点的下标索引
    rightSonIndex=2*index+2
    while leftSonIndex<=len(array)-1:               #大跟堆向下调整的前提是该节点至少存在左儿子节点
        if rightSonIndex>len(array)-1:              #该节点只存在左儿子节点
            if array[leftSonIndex]>array[index]:    #若左儿子节点数值比该节点数值大，就进行交换
                array[index],array[leftSonIndex]=array[leftSonIndex],array[index]
            break                                   #无论是否进行数值交换，都在该轮后跳出循环
        else:                                            #该节点同时存在左右儿子节点
            if array[leftSonIndex]>=array[rightSonIndex]:#找出左右儿子节点所对应数值的较大值
                bigIndex=leftSonIndex
            else:
                bigIndex=rightSonIndex
            if array[bigIndex] > array[index]:       #若该节点数值比儿子节点的较大值小，就进行交换
                array[index], array[bigIndex] = array[bigIndex], array[index]
                index=bigIndex                       #交换后，更新节点信息
                leftSonIndex = 2 * index + 1         #左右儿子节点的下标索引
                rightSonIndex = 2 * index + 2
            else:                                    #若该节点数值比儿子节点的较大值还大，则不需要进行交换，直接跳出循环
                break

################小根堆模块：建立小根堆、调整小根堆################
#建立小跟堆
def smallHeapInsert(array,index):
    parentIndex=(index-1)//2             #父节点的下标索引
    while parentIndex>=0 and array[index]<array[parentIndex]:
        array[index],array[parentIndex]=array[parentIndex],array[index]
        index=parentIndex                #交换后，更新节点信息
        parentIndex = (index - 1) // 2

#调整小根堆
def smallHeapeapIfy(array,index):
    leftSonIndex=2*index+1                          #左右儿子节点的下标索引
    rightSonIndex=2*index+2
    while leftSonIndex<=len(array)-1:               #小跟堆向下调整的前提是该节点至少存在左儿子节点
        if rightSonIndex>len(array)-1:              #该节点只存在左儿子节点
            if array[leftSonIndex]<array[index]:    #若左儿子节点数值比该节点数值小，就进行交换
                array[index],array[leftSonIndex]=array[leftSonIndex],array[index]
            break                                   #无论是否进行数值交换，都在该轮后跳出循环
        else:                                            #该节点同时存在左右儿子节点
            if array[leftSonIndex]<=array[rightSonIndex]:#找出左右儿子节点所对应数值的较小值
                smallIndex=leftSonIndex
            else:
                smallIndex=rightSonIndex
            if array[smallIndex] < array[index]:     #若该节点数值比儿子节点的较小值大，就进行交换
                array[index], array[smallIndex] = array[smallIndex], array[index]
                index=smallIndex                     #交换后，更新节点信息
                leftSonIndex = 2 * index + 1         #左右儿子节点的下标索引
                rightSonIndex = 2 * index + 2
            else:                                    #若该节点数值比儿子节点的较小值还小，则不需要进行交换，直接跳出循环
                break


#函数功能：找到数据流的中位数
def StreamMedian(array):
    bigHeap=[]                           #初始化一个大根堆和小根堆
    smallHeap=[]
    for index in range(len(array)):      #逐步读取数据流数据
        if index==0:                     #读取第一个数据时，默认将数据放入大根堆
            bigHeap.append(array[index])
        else:                             #读取数据流其余数据时候
            #若新读取的数值比大根堆头结点（大根堆最大值）大，那将该数放入小根堆
            # 反之，那将该数放入大根堆
            if array[index]>bigHeap[0]:
                smallHeap.append(array[index])
                smallHeapInsert(smallHeap,len(smallHeap)-1)
            else:
                bigHeap.append(array[index])
                bigHeapInsert(bigHeap,len(bigHeap)-1)

        #大根堆的长度和小根堆的长度相差不能超过2
        if len(bigHeap)>=len(smallHeap)+2:                 #大根堆的长度比小根堆的长度长2以上
            #大根堆的头结点和尾节点先进行交换
            bigHeap[len(bigHeap)-1],bigHeap[0]=bigHeap[0],bigHeap[len(bigHeap)-1]
            smallHeap.append(bigHeap.pop())             #再将大根堆的尾节点移到小根堆上
            smallHeapInsert(smallHeap,len(smallHeap)-1) #分别对大、小根堆进行堆调整
            bigHeapeapIfy(bigHeap,0)
        elif len(bigHeap)+2<=len(smallHeap):            #小根堆的长度比大根堆的长度长2以上
            # 小根堆的头结点和尾节点先进行交换
            smallHeap[len(smallHeap) - 1], smallHeap[0] = smallHeap[0], smallHeap[len(smallHeap) - 1]
            bigHeap.append(smallHeap.pop())             #再将小根堆的尾节点移到大根堆上
            smallHeapeapIfy(smallHeap, 0)               #对大、小根堆进行堆调整
            bigHeapInsert(bigHeap, len(bigHeap) - 1)

    #如果数据流中读出奇数个数值，那么中位数就是所有数值排序之后的位于中间的数值
    #如果数据流中读出偶数个数值，那么中位数就是所有数值排序之后的中间两个数的平均值
    if len(array) %2 !=0:  #数据流的个数为奇数
        if len(bigHeap)>len(smallHeap):
            return bigHeap[0]
        else:
            return smallHeap[0]
    else:                  #数据流的个数为偶数
        return (bigHeap[0]+smallHeap[0])/2


######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找出数据流的中位数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                       # 随机数列表的长度
        array = randomList(length)         # 生成随机数列表

        # 如果数据流中读出奇数个数值，那么中位数就是所有数值排序之后的位于中间的数值
        # 如果数据流中读出偶数个数值，那么中位数就是所有数值排序之后的中间两个数的平均值
        if len(array)%2==0:
            right=(array[len(array)//2]+array[len(array)//2-1])/2
        else:
            right=array[len(array)//2]
        test=StreamMedian(array)
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))