import copy


class Solution:
    def permutation(self, s: str) -> List[str]:
        string = list(s)       # 将字符串转化为列表
        length = len(string)   # 字符串长度
        pb = [False] * length  # 布尔数组，记录当前字符是否已经加入字符串

        self.result = []       # 字符串的组合
        self.data = {}         # 去重处理，防止重复添加字符串
        for index in range(len(string)):
            self.dfs(pb, string, 0, [], length)
        return self.result

    def dfs(self, pb, string, index, arr, length):
        if index == length:
            res = ''.join(arr)
            if res not in self.data:
                self.result.append(copy.copy(res))
                self.data[copy.copy(res)] = 1
            return

        for i in range(length):
            if pb[i] == False:
                pb[i] = True
                arr.append(string[i])
                self.dfs(pb, string, index + 1, arr, length)
                arr.pop()
                pb[i] = False