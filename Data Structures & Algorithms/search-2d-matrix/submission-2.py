class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LL, RR = 0, len(matrix) - 1

        while LL <= RR:
            MM = (LL + RR) // 2
            if matrix[MM][0] > target:
                RR = MM - 1
            elif matrix[MM][-1] < target:
                LL = MM + 1
            else:
                break
        if not LL <= RR:
            return False
        row = (LL + RR) // 2
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
         