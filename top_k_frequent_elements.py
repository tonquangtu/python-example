from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        for item in nums:
            count = map.get(item, None)
            if count is None:
                map[item] = 1
            else:
                map[item] = count + 1

        




