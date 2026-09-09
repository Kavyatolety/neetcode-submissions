class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)): # i = 0
            if nums[i] == target:
                return i
            else:
                i = i+1
        return -1

        