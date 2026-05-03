class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, index]
        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[len(stack) - 1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append([temp, ind])
        return res
