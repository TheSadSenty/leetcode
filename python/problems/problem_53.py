class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result: int = nums[0]
        max_ending: int = nums[0]

        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i])
            result = max(result, max_ending)
        return result
