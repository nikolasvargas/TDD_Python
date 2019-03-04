from domain import User, Bid, Sale
import unittest

class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.testcase1 = User('john')
        self.testcase2 = User('angel')
        self.from_sale = Sale('Phone')

    def test_higher_and_lower_value_wagered_in_ascending_order(self):
        john_bid = Bid(self.testcase1, 100)
        angel_bid = Bid(self.testcase2, 200)

        LOWER_EXPECTED_VALUE = 100
        HIGHER_EXPECTED_VALUE = 200

        self.from_sale.to_bet(john_bid)
        self.from_sale.to_bet(angel_bid)
        self.assertEqual(LOWER_EXPECTED_VALUE, self.from_sale.lowest_bid)
        self.assertEqual(HIGHER_EXPECTED_VALUE, self.from_sale.higher_bid)

    def test_highest_and_lowest_value_whit_more_than_two_bets(self):
        from random import randrange

        total_bids = []
        LOWER_EXPECTED_VALUE = 100
        HIGHER_EXPECTED_VALUE = 1000

        for _ in range(randrange(3, 300)):
            total_bids.append(Bid(self.testcase1, 100))
            total_bids.append(Bid(self.testcase2, 1000))

        for bid in total_bids:
            self.from_sale.to_bet(bid)

        self.assertEqual(LOWER_EXPECTED_VALUE, self.from_sale.lowest_bid)
        self.assertEqual(HIGHER_EXPECTED_VALUE, self.from_sale.higher_bid)

    def test_return_same_value_when_sale_have_one_bid(self):
        user_test_case = User('alone')
        alone_bid = Bid(user_test_case, 5000)

        EXPECTED_VALUE = 5000

        self.from_sale.to_bet(alone_bid)
        self.assertEqual(EXPECTED_VALUE, self.from_sale.lowest_bid)
        self.assertEqual(EXPECTED_VALUE, self.from_sale.higher_bid)

if __name__ == "__main__":
    unittest.main()