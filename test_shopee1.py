import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype
		"""
        if not nums:
            return None
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappushpop(min_heap, n)
        return min_heap[0]


test_nums = [1, 3, 5, 9, 100, 28, 12]
s = Solution()
res = s.findKthLargest(test_nums, 3)
print(res)

# raw_input = input()
# arr = str.split(raw_input)
# nums_str = arr[0]
# k = arr[1]

#  [1, 2, 3, 4, 5]
arr_str = "[1, 2, 3, 4, 5]"
arr_str = arr_str[1: len(arr_str) - 1]


print(arr_str)





# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None