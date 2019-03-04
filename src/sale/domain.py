import sys

class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class Bid:
    def __init__(self, user: User, value):
        self.user = user
        self.value = value

class Sale:
    def __init__(self, description):
        self.description = description
        self.__bids = []

    @property
    def bids(self):
        return self.__bids

class Classifier:
    def __init__(self):
        self.higher_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    def evaluate_bid(self, sale: Sale):
        for bid in sale.bids:
            if bid.value > self.higher_bid:
                self.higher_bid = bid.value
            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value
