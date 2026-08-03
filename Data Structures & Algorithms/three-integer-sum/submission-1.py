class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums): # i = index, a = value
            if a > 0: # where the first number is greater than zero
                break
            if i > 0 and a == nums[i-1]: # checking for duplicates
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                if a + nums[l] + nums[r] == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return res


                


        
