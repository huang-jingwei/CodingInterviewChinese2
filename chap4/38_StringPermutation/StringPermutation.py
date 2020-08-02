class Solution:
    def __init__(self):
        self.res = []                   # 用来存放字符串的全排列

    def permutation(self, s: str) -> List[str]:
        string = list(s)                # 将字符串数据转成列表格式

        if len(string) == 1:
            return string
        elif len(string) == 0:
            return None

        self.dfs(string, 0)             # 开始深度优先遍历
        return self.res

    # 深度优先遍历
    def dfs(self, string, index):
        if index == len(string) - 1:    # 已经遍历到最后一位了， 添加排列方案
            res = ""                    # 将字符列表组合成字符串，因为在之前将字符串转化成字符列表
            for i in string:
                res += i
            self.res.append(res)
            return

        dirct = {}                      # 用来记录该字符在之前是否出现过
        for i in range(index, len(string)):

            if string[i] in dirct:      # 该字符在之前已经存在过了
                continue
            dirct[string[i]] = 1
            string[i], string[index] = string[index], string[i]  # 交换两个字符
            self.dfs(string, index + 1)                          # 开始固定index+1位
            string[i], string[index] = string[index], string[i]  # 恢复之前的字符交换