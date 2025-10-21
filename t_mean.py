from mean import mean 


def test_int():
    # test a list of ints
    num_list = [1, 2, 3, 4, 5]
    assert mean(num_list) == 3


def test_zero():
    # test a list containing a zero
    num_list = [0, 2, 4, 6]
    assert mean(num_list) == 3


def test_float():
    # test a list whose mean is a float
    num_list = [1, 2, 3, 4]
    assert mean(num_list) == 2.5


def test_big():
    # test some big numbers
    big = 100_000_000
    assert mean(range(1, big)) == big/2.0
