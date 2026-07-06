class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = set()

        last_dup_idx = -1
        for i in range(len(nums)):
            if nums[i] not in unique_nums:
                if last_dup_idx != -1:
                    nums[last_dup_idx] = nums[i]
                    last_dup_idx += 1
                unique_nums.add(nums[i])
            elif last_dup_idx == -1:
                    last_dup_idx = i
        return len(unique_nums)