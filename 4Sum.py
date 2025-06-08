class Solution(object):
    def fourSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if abs(total - target) < abs(closest_sum - target):
                        closest_sum = total

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        return total  # Exact match
        return closest_sum