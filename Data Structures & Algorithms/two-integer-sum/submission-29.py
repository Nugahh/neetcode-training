class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            print(diff)
            if diff in myMap:
                return [myMap[diff], i]
            myMap[num] = i
            print("myMap num ", myMap[num])
