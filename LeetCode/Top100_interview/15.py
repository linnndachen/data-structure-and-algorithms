class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        nums.sort()
        
        if length < 3:
            return []
        for i in range(length):
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
        
    def twoSum(self, nums, i, res):
        low, high = i+1, len(nums) - 1
        while (low < high):
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                #avoid repetition
                while low < high and nums[low] == nums[low-1]:
                    low += 1
        return res
    #[-2,0,0,2,2]
    #[[-2,0,2],[-2,0,2]]