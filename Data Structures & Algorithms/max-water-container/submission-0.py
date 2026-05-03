class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            res = max(res, area)
            if heights[L] <= heights[R]:
                L += 1
            elif heights[L] >= heights[R]:
                R -= 1
        return res