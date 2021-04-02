class Solution:

    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True

        # step1：弹出头结点
        heaVal = postorder.pop()
        index = 0
        length = len(postorder)

        # step2：找到左子树、右子树的分界点
        # index:为右子树的第一个节点的下标
        while index < length:
            if postorder[index] < heaVal:
                index += 1
            else:
                break

        # 右子树上的所有节点都必须必头节点大
        if index < length:
            for i in range(index, length):
                if postorder[i] <= heaVal:
                    return False

        # 递归进行迭代判断
        return self.verifyPostorder(postorder[:index]) and self.verifyPostorder(postorder[index:])