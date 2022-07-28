from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        i, j = 0, 0
        new_arr = []
        while i < l1 or j < l2:
            if i < l1 and j < l2 and nums1[i] < nums2[j] or i < l1 and not j < l2:
                new_arr.append(nums1[i])
                i += 1
            elif j < l2:
                new_arr.append(nums2[j])
                j += 1
        l3 = l1 + l2
        mid = l3 // 2
        if l3 % 2 != 0:
            arr = new_arr[mid: mid + 1]
        else:
            arr = new_arr[mid - 1: mid + 1]
        return sum(arr) / len(arr)

c = Solution()

print(c.findMedianSortedArrays([1, 5, 15], [8, 26, 37]))