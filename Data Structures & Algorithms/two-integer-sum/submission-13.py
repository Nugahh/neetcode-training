class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            reverse = target - n
            if reverse in seen:
                return [seen[reverse], i]
            seen[n] = i