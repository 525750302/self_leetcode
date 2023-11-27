#
# @lc app=leetcode.cn id=1357 lang=python
#
# [1357] 每隔 n 个顾客打折
#

# @lc code=start
class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.prices = {}
        for i in products:
            self.prices[i] = prices[products.index(i)]
        self.cnt = 0


    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.cnt += 1
        get_discount = 0
        if self.cnt % self.n == 0:
            get_discount = self.discount
        sum_val = sum([self.prices[product[i]] * amount[i] for i in range(len(product))])

        return sum_val - sum_val * get_discount / 100.0



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
# @lc code=end

