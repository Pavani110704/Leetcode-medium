class Solution(object):
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2
