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
        self.higher_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max
        self.__bids = []

    @property
    def bids(self):
        """return a list copy of bids"""
        return list(self.__bids)

    def to_bet(self, user_bids: Bid):
        if(self.bettor_can_play(user_bids)):
            if user_bids.value > self.higher_bid:
                self.higher_bid = user_bids.value
            if user_bids.value < self.lowest_bid:
                self.lowest_bid = user_bids.value

            self.__bids.append(user_bids)
        else:
            raise ValueError('Error to bet, check valid conditions')

    def bettor_can_play(self, bettor: Bid):
        nobody_bet = True if not self.__bids else False
        if nobody_bet:
            return True
        else:
            bet_is_greater_than_last = bettor.value > self.__bids[-1].value
            is_not_same_bettor = self.__bids[-1].user != bettor.user
            return is_not_same_bettor and bet_is_greater_than_last
