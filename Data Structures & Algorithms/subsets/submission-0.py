class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            [nums[n]
                for n in range(0, len(nums))
                if (i >> n & 1 == 1)
            ]
            for i in range(0, 2**len(nums))
        ]
        