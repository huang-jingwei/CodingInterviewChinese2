#主函数入口
#打印字符串的全部子序列
def AllSubsquences(string):
    if string==None:     #判断输入字符串是否为空字符串
        print("the String is null")
        return None
    else:                #输入字符串不为空时，进入打印字符串全部子序列的函数
        return PrintAllSubsquences(string=string,index=0,res="")


#string:原始字符串
#index：当前递归到字符串哪一位
#res：上一步递归得到的子序列
def PrintAllSubsquences(string,index,res):
    if index>=len(string):  #递归到字符串的最后位
        print(res)
        return
    else:
        PrintAllSubsquences(string,index+1,res)              #index位不加当前字符
        PrintAllSubsquences(string, index+1, res+string[index])#index位添加当前字符