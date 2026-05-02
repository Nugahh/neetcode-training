class Solution:
    def prefixProd(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 1
        for n in nums:
            total *= n
            prefix.append(total)
        return prefix

    def suffixProd(self, nums: List[int]) -> List[int]:
        suffix = []
        total = 1
        for n in reversed(nums):
            total *= n
            suffix.append(total)
        left, right = 0, len(suffix) - 1
        while left < right:
            suffix[left], suffix[right] = suffix[right], suffix[left]
            left += 1
            right -= 1
        return suffix

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = self.prefixProd(nums)
        suffix = self.suffixProd(nums)

        start = 0
        end = len(nums) - 1

        for i, n in enumerate(nums):
            if i == 0:
                res.append(suffix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * suffix[i + 1])
        return res
