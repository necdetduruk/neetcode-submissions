class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            completent = target - num
            if completent in prevMap:
                return [prevMap[completent], i]
            prevMap[num] = i
        