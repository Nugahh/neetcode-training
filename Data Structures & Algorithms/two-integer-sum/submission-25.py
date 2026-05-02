class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in myMap:
                print(diff)
                return [myMap[diff], i]
            myMap[num] = i
