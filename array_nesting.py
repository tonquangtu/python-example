from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 1
        mark = [False for x in nums]

        for i in range(0, len(nums)):
            count = 0
            index = i
            while nums[index] != index and mark[index] is False:
                count += 1
                mark[index] = True
                index = nums[index]

            if count > max_length:
                max_length = count

        return max_length


solution = Solution()
test_nums = [5, 4, 0, 3, 1, 6, 2]
res = solution.arrayNesting(test_nums)
print(res)





