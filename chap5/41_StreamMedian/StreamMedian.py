import random

################大根堆模块：建立大根堆、调整大根堆################
#建立大根堆
def bigHeapInsert(array,index):
    parentIndex=(index-1)//2       #父节点的下标索引
    while parentIndex>=0 and array[parentIndex]<array[index]:
        array[index],array[parentIndex]=array[parentIndex],array[index]
        index=parentIndex
        parentIndex = (index - 1) // 2

#调整大根堆
def bigHeapeapIfy(array,index):
    leftSonIndex=2*index+1                          #左右儿子节点的下标索引
    rightSonIndex=2*index+2
    while leftSon<=len(array)-1:                    #大跟堆向下调整的前提是该节点至少存在左儿子节点
        if rightSonIndex>len(array)-1:              #该节点只存在左儿子节点
            if array[leftSonIndex]>array[index]:    #若左儿子节点数值比该节点数值大，就进行交换
                array[index],array[leftSonIndex]=array[leftSonIndex],array[index]
            break
        elif rightSonIndex<=len(array)-1:                #该节点同时存在左右儿子节点
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
        index=parentIndex
        parentIndex = (index - 1) // 2

#调整大根堆
def smallHeapeapIfy(array,index):
    leftSonIndex=2*index+1                          #左右儿子节点的下标索引
    rightSonIndex=2*index+2
    while leftSon<=len(array)-1:                    #小跟堆向下调整的前提是该节点至少存在左儿子节点
        if rightSonIndex>len(array)-1:              #该节点只存在左儿子节点
            if array[leftSonIndex]<array[index]:    #若左儿子节点数值比该节点数值小，就进行交换
                array[index],array[leftSonIndex]=array[leftSonIndex],array[index]
            break
        elif rightSonIndex<=len(array)-1:                #该节点同时存在左右儿子节点
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

def StreamMedian(array):
    bigHeap=[]                                   #初始化一个大根堆和小根堆
    smallHeap=[]

    for index in range(len(array)):

        if index==0:                            # 一开始先将数据放入大根堆
            bigHeap.append(array[index])
        else:                                        #其余情况下
            if array[index]>bigHeap[0]:              #
                smallHeap.append(array[index])
                smallHeapInsert(smallHeap,len(smallHeap)-1)
            else:
                bigHeap.append(array[index])







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