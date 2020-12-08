class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        This is my original solution. It works but it is slow
        """
        if upper == lower:
            if lower not in nums:
                nums.append(str(lower))
                return nums
            return []
        ranges = []
        nums.append(upper+1)
        nums.insert(0, lower-1)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ranges.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                low = nums[i] + 1
                high = nums[i+1] - 1
                missing_range = '{}->{}'.format(low, high)
                ranges.append(missing_range)
        return ranges
    
    def shorten (self, nums, lower, upper):
        """
        Then I realzed, since I have already added the lower and upper in the list, the first case has already been included.
        """
        ranges = []
        nums = [lower-1] + nums + [upper+1]
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ranges.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                low = nums[i] + 1
                high = nums[i+1] - 1
                missing_range = '{}->{}'.format(low, high)
                ranges.append(missing_range)
        return ranges
