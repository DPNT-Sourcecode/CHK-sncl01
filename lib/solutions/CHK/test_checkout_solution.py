from .checkout_solution import checkout


def test_checkout_solution():
    assert checkout("NOT AN ITEM") == -1

    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("E") == 40

    assert checkout("AAA") == 130
    assert checkout("AAAAA") == 200
    assert checkout("BB") == 45

    assert checkout("AAABBACBB") == 290
    assert checkout("AAABBACBBEE") == 275