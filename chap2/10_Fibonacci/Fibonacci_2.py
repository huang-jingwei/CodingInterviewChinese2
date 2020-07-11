
#函数功能：斐波那契数列,输出数列的第k项
#算法复杂度:O(N)

def Fibonacci(k):
    if k<0:            #k为非负整数，当输入的k为负数时，直接输出false
        return False
    if k==0:           #当k=0、1、2时，直接输出对应数值
        return 0
    elif k==1:
        return 1
    elif k==2:
        return 2
    else:              #当k>1时，采用数组形式来记录斐波那契数列数值
        array=[0]*(k+1)
        array[1]=1
        array[2]=2
        for index in range(2,len(array)):
            array[index]=array[index-1]+array[index-2]
        return array[k]

if __name__=="__main__":
    print(Fibonacci(50))
