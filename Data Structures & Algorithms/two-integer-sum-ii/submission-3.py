class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        res = []
        while l<r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                res = [l+1, r+1]
                l+=1
                r-=1
            elif two_sum < target:
                l += 1
            else:
                r -= 1
        return res
                
        


        