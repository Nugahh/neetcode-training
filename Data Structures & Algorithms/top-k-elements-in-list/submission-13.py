class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myList = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            myList[n] = myList.get(n, 0) + 1
        for value, count in myList.items():
            freq[count].append(value)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                    return res
        # res = 
        # for i, n in myList.items():
        #     res[i] = n
        
        