class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        # put in a dict as number as key and count as value
        for num in nums:
            count[num] += 1
        print(count)
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            