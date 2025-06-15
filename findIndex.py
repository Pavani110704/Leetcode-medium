class Solution:
    def searchRange(self, nums, target):
        def find(bound):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < target or (bound and nums[m] == target):
                    l = m + 1
                else:
                    r = m
            return l

        left = find(False)
        right = find(True) - 1
        if left <= right and right < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]
