from collections import defaultdict

class PairManager:

    def __init__(self, threshold):
        self.threshold = threshold
        # Default value is 0
        self.prices = defaultdict(int)
        # Default value is an empty set 
        self.pairs = defaultdict(set)
    
    def update_price(self, stock, new_price):
        self.prices[stock] = new_price
        for pair in self.pairs[stock]:
            if pair in self.prices and abs(self.prices[stock] - self.prices[pair]) > self.threshold:
                self.notify(stock, self.prices[stock], pair, self.prices[pair])
    
    def register(self, stock1, stock2):
        # Dict of sets handles duplicates automatically
        self.pairs[stock1].add(stock2)
        self.pairs[stock2].add(stock1)

    def notify(self, stock1, price1, stock2, price2):
        # Not implemented by me in the OA
        pass