class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {v: i for i,v in enumerate(nums)}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap and hmap[diff] != i:
                return [i, hmap[diff]]
        return []
