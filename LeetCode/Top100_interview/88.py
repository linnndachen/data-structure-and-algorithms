class Solution:
    # Time - O(n+m)log(n+m)
    #Space - O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)

    def pointer_front(self, nums1, m, nums2, n):
        """
        This method the pointer starts from the begining and start comparing
        Time - O(n+m)
        Space - O1
        """
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

        return nums1

    def pointer_back(self, nums1, m, nums2, n):
        """
        This method the pointers start from the end of the two lists
        Time - O(n+m)
        Space - O1
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]
        return nums1

    def wrong_solution(self, nums1, m, nums2, n):
        """
        This was my initial solution.
        This is wrong because for example if
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        I get - [1,2,2,1,2,3,1,2,3]
        without a pointer, I will just reapeatly add the the smallest 3 numbers
        """
        nums1_copy = nums1[:m]
        nums1[:] = []

        for i in range(n):
            for j in range(m):
                if nums2[i] > nums1_copy[j]:
                    nums1.append(nums1_copy[j])
                else:
                    nums1.append(nums2[i])
        return nums1
