class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = set()

        left_ptr = 0
        for i in range(len(nums)):
            if nums[i] not in unique_nums:
                nums[left_ptr] = nums[i]
                left_ptr += 1
                unique_nums.add(nums[i])
        return len(unique_nums)