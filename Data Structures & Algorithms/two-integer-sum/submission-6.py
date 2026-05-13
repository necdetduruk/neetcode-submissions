class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, val in enumerate(nums):
            completent = target - val
            if completent in hashmap:
                return [hashmap[completent], index]
            hashmap[val] = index
        