class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of the first n natural numbers formula
        actual_sum = sum(nums)
        return expected_sum - actual_sum
