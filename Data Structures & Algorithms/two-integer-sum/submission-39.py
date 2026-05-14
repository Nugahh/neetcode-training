class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in seen:
                return [seen[n], i]
            seen[diff] = i
                