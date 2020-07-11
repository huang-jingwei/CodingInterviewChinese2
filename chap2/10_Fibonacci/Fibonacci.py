import  numpy as np
#函数功能：斐波那契数列,输出数列的第k项
#算法复杂度:O(N)

def Fibonacci(k):
    if k<=0:
        return False
    if k==1:
        return 1
    elif k==2:
        return 1
    else:
        array=[1]*k
        for index in range(2,k):
            array[index]=array[index-1]+array[index-2]
        return array[k-1]

if __name__=="__main__":
    print(Fibonacci(20))



