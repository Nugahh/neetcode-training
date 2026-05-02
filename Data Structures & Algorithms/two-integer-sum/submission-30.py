class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict(list)

        # on insère tout d'abord
        for i, num in enumerate(nums):
            myMap[num].append(i)

        # puis on vérifie
        for i, num in enumerate(nums):
            diff = target - num
            if diff in myMap:
                # évite de matcher num avec lui-même
                if diff != num:
                    return [i, myMap[diff][0]]
                elif len(myMap[num]) > 1:
                    return [myMap[num][0], myMap[num][1]]