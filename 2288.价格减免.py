#
# @lc app=leetcode.cn id=2288 lang=python
#
# [2288] 价格减免
#

# @lc code=start
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        
        def is_number(s: str) -> bool:
            try:
                int(s)
                return True
            except ValueError:
                return False

        return ' '.join(map(lambda x: '$' + "{:.2f}".format((int(x[1:]) * (1-discount * 0.01))) if x.startswith('$') and is_number(x[1:]) else x, sentence.split()))
# @lc code=end

