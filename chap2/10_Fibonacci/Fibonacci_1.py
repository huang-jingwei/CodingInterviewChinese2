class Solution:
    def fib(self, n: int) -> int:
        array = []
        array.append(0)
        array.append(1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            array = []
            for i in range(n + 1):
                array.append(None)
            array[0] = 0
            array[1] = 1
            for i in range(2, n + 1):
                array[i] = (array[i - 1] + array[i - 2]) % 1000000007
            return array[n]