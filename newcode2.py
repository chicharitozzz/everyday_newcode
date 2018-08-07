class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.s = ''
        self.d = {}

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return sel.stack2.pop()

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        merge_list = None
        if pHead1.val < pHead2.val:
            merge_list = pHead1
            merge_list.next = self.Merge(pHead1.next, pHead2)

        else:
            merge_list = pHead2
            merge_list.next = self.Merge(pHead1, pHead2.next)

        return merge_list

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)

        max_sum = float('-inf')
        # for j in range(length):
        #     tmp = 0
        #     for k in range(j, length):
        #         tmp += array[k]
        #         if tmp > max_sum:
        #             max_sum = tmp

        cur_sum = 0
        for i in range(length):
            if cur_sum <= 0:
                cur_sum = array[i]

            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum

    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        import string
        digs = string.digits

        symbol, decimal, scientific = False, False, False
        length = len(s)

        for i in range(length):
            if s[i] == 'e' or s[i] == 'E':
                if i == length - 1:
                    return False
                elif scientific:
                    return False
                scientific = True

            elif s[i] == '+' or s[i] == '-':
                if symbol and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False  # 正负号跟在e后
                elif not symbol and i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                symbol = True

            elif s[i] == '.':
                if scientific or decimal:
                    return False
                decimal = True

            elif s[i] not in digs:
                return False

        return True

    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.d[c] == 1:
                return c

        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        self.d[char] = self.d.get(char, 0) + 1

    def myPow(self, x, n):
        if n == 0:
            return 1

        elif n < 0:
            n = -n
            x = 1 / x

        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        遍历一遍找到最高点，然后从左右两边分别向最高点进发
        """
        length = len(height)

        if length <= 2:
            return 0

        max_height = 0
        ind = -1

        for i in range(length):
            if height[i] > max_height:
                max_height = height[i]
                ind = i

        area, root = 0, height[0]

        for i in range(ind):
            if root <= height[i]:
                root = height[i]

            else:
                area += (root - height[i])

        root = height[length - 1]
        for j in range(length - 1, ind, -1):
            if root <= height[j]:
                root = height[j]
            else:
                area += (root - height[j])

        return area


if __name__ == '__main__':
    s = Solution()
    # s.Insert('g')
    # r = s.FirstAppearingOnce()
    # r = s.myPow(2.0000, -2)
    r = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(r)
