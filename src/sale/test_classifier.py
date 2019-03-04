from unittest import TestCase
from domain import User, Bid, Sale, Classifier

class TestClassifier(TestCase):
    def test_bids(self):
        from_sale = Sale('Phone')

        testcase1 = User('john')
        testcase2 = User('angel')

        john_bid = Bid(testcase1, 100)
        angel_bid = Bid(testcase2, 200)

        from_sale.bids.append(john_bid)
        from_sale.bids.append(angel_bid)

        lower_expected_value = 100
        higher_expected_value = 200

        a1 = Classifier()
        a1.evaluate_bid(from_sale)
        
        self.assertEqual(lower_expected_value, a1.lowest_bid)
        self.assertEqual(higher_expected_value, a1.higher_bid)

if __name__ == "__main__":
    import unittest
    unittest.main()