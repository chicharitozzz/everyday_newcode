# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        """二维数组中的查找"""
        # write code here
        i, j = len(array) - 1, 0  # 从左下角开始找
        col_num = len(array[i])
        while j < col_num and i >= 0:
            if target > array[i][j]:
                j += 1  # 目标数大于当前数，向右找
            elif target < array[i][j]:
                i -= 1  # 目标数小于当前数，向上找
            else:
                return True
        return False

    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # return s.replace(' ', '%20')
        length = len(s)
        s_new = ''
        for i in range(length):
            if s[i] == ' ':
                s_new += '%20'
            else:
                s_new += s[i]
        return s_new

    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        else:
            # a, b, c = 0, 0, 1
            # for _ in range(n - 1):
            #     a = b + c
            #     b, c = c, a
            # print(a)
            # return a
            b, c = 0, 1
            for _ in range(n - 1):
                c += b
                b = c - b
            # print(c)
            return c

    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            b, c = 1, 2
            for _ in range(number - 2):
                c += b
                b = c - b
            return c

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # for i in range(len(rotateArray) - 1):
        #     if rotateArray[i + 1] < rotateArray[i]:
        #         print(rotateArray[i + 1])
        #         return rotateArray[i + 1]
        # return 0

        if not rotateArray:
            return 0
        # tmp = 0
        # for num in rotateArray:
        #     if num < tmp:
        #         return num
        #     tmp = num

        left, right = 0, len(rotateArray) - 1
        while left < right - 1:
            mid = left + right >> 1
            if rotateArray[mid] > rotateArray[left]:
                left = mid
            elif rotateArray[mid] < rotateArray[left]:
                right = mid

        # print(rotateArray[right])
        return rotateArray[right]

    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        b, c = 1, 2
        for _ in range(number - 2):
            c += b
            b = c - b

        # print(c)
        return c

    def reOrderArray(self, array):
        # write code here
        length = len(array)
        odd_list = []
        even_list = []
        for i in range(length):
            if array[i] % 2 != 0:
                odd_list.append(array[i])
            else:
                even_list.append(array[i])

        res = odd_list + even_list
        print(res)
        return res

    def FindKthToTail(self, head, k):
        # write code here
        list_node = []

        while head:
            list_node.append(head)
            head = head.next

        if k > len(list_node) or k < 1:
            return
        return list_node[-k]

    def ReverseList(self, pHead):
        # write code here
        list_node = []
        while pHead:
            list_node.append(pHead)
            pHead = pHead.next

        return list_node[::-1]

    def Power(self, base, exponent):
        # write code here
        res = 1

        if exponent == 0:
            return 1

        elif base == 0:
            return 0

        # elif exponent > 0:
        #     while exponent > 0:
        #         res *= base
        #         exponent -= 1

        # elif exponent < 0:
        #     base = 1 / base
        #     exponent = abs(exponent)
        #     while exponent > 0:
        #         res *= base
        #         exponent -= 1

        flag = True if exponent > 0 else False
        exponent = abs(exponent)
        while exponent > 0:
            res *= base
            exponent -= 1
        if not flag:
            res = 1 / res

        # print(res)
        return res

    def FindNumbersWithSum(self, array, tsum):
        length = len(array)
        left, right = 0, length - 1
        while left < right:
            if array[left] + array[right] == tsum:
                return array[left], array[right]
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1

        return []

    def FindContinuousSequence(self, tsum):
        # write code here
        sat = []
        for t in range(1, int(tsum / 2) + 1):
            n = 1
            while (2 * t + n - 1) * n < 2 * tsum:
                n += 1

            if (2 * t + n - 1) * n == 2 * tsum:
                sat.append((t, n))

        length = len(sat)

        res = [[] for _ in range(length)]

        for i in range(length):
            for x in range(sat[i][0], sat[i][0] + sat[i][1]):
                res[i].append(x)

        print(res)
        return res

    def LeftRotateString(self, s, n):
        # write code here
        length = len(s)
        s_left = s[n:]
        s_right = s[:n]

        # print(s_left + s_right)

        return s_left + s_right

    def ReverseSentence(self, s):
        # write code here
        sl = s.split(' ')[::-1]
        return ' '.join(sl)

    def IsContinuous(self, numbers):
        # write code here
        num = len(numbers)
        if num != 5:
            return False

        count_0 = 0
        for i in range(num):
            mnum = numbers[i]
            tmp = i
            for j in range(i + 1, num):
                if numbers[j] < mnum:
                    mnum = numbers[j]
                    tmp = j

            if mnum == 0:
                count_0 += 1

            numbers[i], numbers[tmp] = numbers[tmp], numbers[i]

        if numbers[0] < 0 or numbers[4] > 13:
            return False

        if count_0 == 0:
            for i in range(num - 1):
                if numbers[i + 1] - numbers[i] != 1:
                    return False
            return True

        elif count_0 == 1:
            difference_2 = 0
            for i in range(1, num - 1):
                if numbers[i + 1] - numbers[i] == 1:
                    continue
                elif numbers[i + 1] - numbers[i] == 2:
                    difference_2 += 1
                    if difference_2 > 1:
                        return False
                else:
                    return False

            return True

        elif count_0 == 2:
            difference_1, difference_2, difference_3 = 0, 0, 0
            for i in range(2, num - 1):
                if numbers[i + 1] - numbers[i] == 1:
                    difference_1 += 1

                elif numbers[i + 1] - numbers[i] == 2:
                    difference_2 += 1

                elif numbers[i + 1] - numbers[i] == 3:
                    difference_3 += 1

            if difference_1 == 2:
                return True

            if difference_2 == 2:
                return True

            if difference_1 == 1 and difference_3 == 1:
                return True

            else:
                return False

        elif count_0 == 3:
            if numbers[4] - numbers[3] == 4:
                return True
            else:
                return False

        elif count_0 == 4:
            return True

    def LastRemaining_Solution(self, n, m):
        # write code here
        # if n == 0:
        #     return -1

        # elif n == 1:
        #     return 0

        # else:
        #     return (self.LastRemaining_Solution(n - 1, m) + m) % n

        if n == 0:
            return -1

        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i

        return res

    def Sum_Solution(self, n):
        # write code here
        return n > 0 and n + self.Sum_Solution(n - 1)

    def FindNumsAppearOnce(self, array):
        # write code here
        # d = {}

        # for n in array:
        #     d[n] = d.get(n, 0) + 1

        # l = sorted(d.items(), key=lambda x: x[1])[:2]

        # res = []
        # for r in l:
        #     res.append(r[0])

        # return res

        def isbit(num, index):
            """判断第index位是1还是0"""
            num >>= index
            return num & 1

        length = len(array)
        tmp = array[0]
        for n in array[1:]:
            tmp ^= n

        index = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            index += 1

        num_1 = 0
        num_0 = 0
        for num in array:
            if isbit(num, index):
                num_1 ^= num

            else:
                num_0 ^= num

        return [num_1, num_0]

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # half = len(numbers) / 2
        # d = {}
        # for n in numbers:
        #     d[n] = d.get(n, 0) + 1
        #     if d[n] > half:
        #         return n

        # return 0

        # 阵地攻守思想
        soilder = numbers[0]
        length = len(numbers)
        count = 1

        for i in range(1, length):
            if numbers[i] != soilder:
                count -= 1
                if count == 0:
                    soilder = numbers[i]
                    count = 1
            else:
                count += 1

        count_s = 0
        for n in numbers:
            if n == soilder:
                count_s += 1

        return soilder if count_s > length / 2 else 0

    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) < 1 or len(s) > 10000:
            return -1

        d = {}
        for symbol in s:
            d[symbol] = d.get(symbol, 0) + 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        d = {}
        for n in numbers:
            d[n] = d.get(n, 0) + 1
            if d[n] > 1:
                duplication[0] = n
                return True

        return False

    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # count = 0
        # i = 1
        # while n // i != 0:
        #     current = (n // i) % 10  # 当前位
        #     before = n // (i * 10)  # 前一位
        #     after = n - (n // i) * i  # 低一位

        #     if current == 0:
        #         count += before * i

        #     elif current == 1:
        #         count += before * i + after + 1

        #     else:
        #         count += (before + 1) * i

        #     i *= 10

        # return count
        count = 0
        i = 1
        while n // i != 0:
            j = i * 10
            count += i * (n // j)

            k = n % j
            if k > (2 * i - 1):
                count += i
            elif k < i:
                count += 0
            else:
                count += k - i + 1

            i = j

        return count

    def Add(self, num1, num2):
        # write code here
        # a = num1 ^ num2
        # b = (num1 & num2) << 1

        # while b != 0:
        #     a, b = a ^ b, (a & b) << 1

        # return a

        while num2 != 0:
            a = num1 & num2
            num1 = (num1 ^ num2) % 0x100000000  # 负数情况
            num2 = (a << 1) % 0x100000000  # 负数情况

        return num1 if num1 <= 0x7FFFFFFF else num1 | (~0x100000000 + 1)


if __name__ == '__main__':
    s = Solution()
    r = s.Add(-2, 2)
    print(r)
