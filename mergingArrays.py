class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        array.sort()
        n = len(array)
        if n % 2 == 0:
            median = (array[n//2 - 1] + array[n//2]) / 2.0
        else:
            median = array[n//2] * 1.0
        return median