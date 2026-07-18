class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3
        for i,v in enumerate(nums):
            bucket[v] += 1
        p = 0
        for i, v in enumerate(bucket):
            for j in range(v):
                nums[p] = i
                p += 1