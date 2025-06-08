class Solution(object):
    def threeSumClosest(self, nums, target):
        closest_sum = None
        min_diff = float('inf')
        
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    diff = abs(total - target)
                    
                    if diff < min_diff:
                        min_diff = diff
                        closest_sum = total
                        
        return closest_sum
