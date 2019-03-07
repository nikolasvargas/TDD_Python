from src.sale.domain import User


def test_add_value_to_user_balance():
    t_user = User('test_add_balance', 100)
    assert t_user.balance == 100
