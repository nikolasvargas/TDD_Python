"""
This module is for training.
Contains unittest also have TDD implementations.
"""

from src.sale.domain import User, Sale, Bid
import pytest

t_user = User('test_add_balance', 100)
product = Sale('bell')


def test_add_value_to_user_balance():
    assert t_user.balance == 100


def test_exception_user_cant_bet_more_than_balance():
    with pytest.raises(ValueError):
        bettor = Bid(t_user, 300)
        bettor.user_can_bet()
