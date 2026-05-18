class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        count = [[] for i in range(len(nums) + 1)]
        res = []

        for i, n in enumerate(nums):
            mp[n] = mp.get(n, 0) + 1
        
        for value, c in mp.items():
            count[c].append(value)
        
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
            if len(res) == k:
                return res
        