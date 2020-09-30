class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def createList(self, nums):
        if len(nums) == 0:
            return None

        head = ListNode(nums[0])
        curr = head

        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            curr.next = node
            curr = node
        return head


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        if not l1 and l2:
            return l2

        if not l2 and l1:
            return l1

        if l1.val <= l2.val:
            l3 = ListNode(l1.val)
            l1 = l1.next
        else:
            l3 = ListNode(l2.val)
            l2 = l2.next

        head = l3

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        else:
            l3.next = l2

        return head

    def print(self, print_list):
        curr = print_list
        while curr is not None:
            print(curr.val)
            curr = curr.next




test_arr = [1, 2, 3, 4]
s = Solution()
list1 = s.createList(test_arr)
s.print(list1)