class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

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


if __name__ == '__main__':
    s = Solution()
    r = s.Merge([], [])
    print(r)
