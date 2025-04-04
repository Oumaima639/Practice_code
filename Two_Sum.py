class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # If no solution is found
        return []  # or you could raise an exception


# Example usage
solution = Solution()
print(solution.twoSum([4, 2, 3], 6))
