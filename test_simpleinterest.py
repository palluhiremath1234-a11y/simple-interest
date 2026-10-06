from simpleinterest import  simple_interest

def test_normal():
    assert simple_interest(5000, 5, 2) == 500


def test_zero():
    assert simple_interest(0, 5, 2) == 0