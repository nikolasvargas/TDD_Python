"""
This module is for training.
Contains unittest also have TDD implementations.
"""

from domain import User, Bid, Sale
import unittest

class TestSale(unittest.TestCase):
    def setUp(self):
        self.testcase1 = User('john')
        self.testcase2 = User('angel')
        self.from_sale = Sale('Phone')

    def test_higher_and_lower_value_wagered_in_ascending_order(self):
        LOWER_EXPECTED_VALUE = 100
        HIGHER_EXPECTED_VALUE = 200

        self.from_sale.to_bet(Bid(self.testcase1, 100))
        self.from_sale.to_bet(Bid(self.testcase2, 200))
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
        EXPECTED_VALUE = 5000

        self.from_sale.to_bet(Bid(User('alone'), 5000))
        self.assertEqual(EXPECTED_VALUE, self.from_sale.lowest_bid)
        self.assertEqual(EXPECTED_VALUE, self.from_sale.higher_bid)

    # if is first bet, allow bettors bet
    # TDD test
    def test_first_bet_amount(self):
        EXPECTED_VALUE = 1
        self.from_sale.to_bet(Bid(self.testcase1, 100))
        self.assertEqual(EXPECTED_VALUE, len(self.from_sale.bids))

    # same bettor can't bet twice in sequence
    # TDD test
    def test_not_be_allow_multiple_bets_in_sequence(self):
        self.from_sale.to_bet(Bid(self.testcase1, 100))
        self.from_sale.to_bet(Bid(self.testcase1, 100))
        user_name_obj_id = [id(bid.user.name) for bid in self.from_sale.bids]
        self.assertNotEqual(user_name_obj_id[0], user_name_obj_id[1])

if __name__ == "__main__":
    unittest.main()