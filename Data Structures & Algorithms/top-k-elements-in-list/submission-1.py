class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countee = Counter(nums)
        top_k = countee.most_common(k)
        return [num for num, _ in top_k]