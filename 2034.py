from sortedcontainers import SortedList

class StockPrice(object):

    def __init__(self):
        self.data_flow = {}
        self.save_date = SortedList()
        self.current_time = None

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if self.current_time == None or timestamp > self.current_time or self.data_flow.get(timestamp,False) ==False :
            self.save_date.add(price)
        else:
            for i in range(len(self.save_date)):
                if self.save_date[i] == self.data_flow[timestamp]:
                    self.save_date.discard(self.data_flow[timestamp])
                    self.save_date.add(price)
                    break
        self.data_flow[timestamp] = price
        if self.current_time == None or self.current_time <timestamp:
            self.current_time = timestamp


    def current(self):
        """
        :rtype: int
        """
        return self.data_flow[self.current_time]


    def maximum(self):
        """
        :rtype: int
        """
        return self.save_date[-1]


    def minimum(self):
        """
        :rtype: int
        """
        return self.save_date[0]
