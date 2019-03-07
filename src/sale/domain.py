import sys


class User:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        print(f'setting value: {value}')
        self._balance = value


class Bid:
    def __init__(self, user: User, value):
        self._user = user
        self._value = value

    @property
    def user(self):
        return self._user

    @property
    def value(self):
        return self._value

    def user_can_bet(self):
        if self._user.balance >= self._value:
            self._user.balance = self._user.balance - self._value
            return True
        else:
            raise ValueError('Insufficient funds')


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
        if self.bettor_can_play(user_bids):
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
            bid_is_greater_than_last = bettor.value > self.__bids[-1].value
            is_not_same_bettor = self.__bids[-1].user != bettor.user
            return (
                is_not_same_bettor and
                bid_is_greater_than_last and
                bettor.user_can_bet()
            )
