class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1
        if digits[-1] > 9 :
            tens = digits[-1] // 10
            ones = digits[-1] % 10
            digits[-1] = ones
            digits[-2] += tens
        else :
            return digits

        return digits

digits = [9,9]
solution = Solution()
tst = solution.plusOne(digits)
print(tst)
