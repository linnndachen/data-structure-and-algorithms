class Solution:
    #Time - N, Space - 1
    def maxSubArray_greedy(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

    #Time - N, Space - 1
    def solution_dp(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)

        return max_sum

    def divide_conquer(self, nums):
        if len(nums) == 1:
            return nums[0]

        # divide the list into two part
        mid = len(nums) // 2

        # the list will become first_half, mid, second_half
        first_half = nums[:mid]
        second_half = nums[mid+1:]

        # Get the consecutive sum around mid element.
        max_consec = nums[mid]
        temp_sum = max_consec

        # get left side max consecutive sum (include mid element)
        curr = mid - 1
        while curr >= 0:
            temp_sum = temp_sum + nums[curr]
            if temp_sum > max_consec:
                max_consec = temp_sum
            curr -= 1

        # get right side max consecutive sum
        curr = mid + 1
        temp_sum = max_consec

        while curr < len(nums):
            temp_sum = temp_sum + nums[curr]
            if temp_sum > max_consec:
                max_consec = temp_sum
            curr += 1

        # compare max_consec with max of first_half, and second_half
        temp_max = max_consec
        if first_half:
            max_first = self.maxSubArray(first_half)
            # compare max_consec with max of first_half
            if temp_max < max_first:
                temp_max = max_first

        if second_half:
            max_second = self.maxSubArray(second_half)
            # compare max_consec with max of second_half
            if temp_max < max_second:
                temp_max = max_second

        return temp_max

        """
        def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   

    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        """