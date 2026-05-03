class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if n + nums[L] + nums[R] > 0:
                    R -= 1
                elif n + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    res.append([n, nums[L],nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res