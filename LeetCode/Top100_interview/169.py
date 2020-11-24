from collections import Counter

class Solution:
    def majorityElement_counter(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.keys(), key=c.get)



    def no_import_dictionary(self,nums):
        table = {}
        for n in nums:
            if n not in table:
                table[n]=1
            else: table[n]+=1
            if table[n] > len(nums)//2:
                return n



    def no_hash(self, nums):
        """
        sort all the values and then check the position
        """
        nums.sort()
        #round down because the position starts with 0
        p = len(nums)//2
        return nums[p]
