class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers)-1
        while l < r:
            sum_lr = numbers[l] + numbers[r]
            if sum_lr == target:
                res = [l+1,r+1]
                l += 1
                r -= 1
            elif sum_lr < target:
                l += 1
            else:
                r -= 1
        return res


        