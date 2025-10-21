from example import example # get the example() function from the example module
import pytest

def test_example():
    with pytest.raises(IndexError):
        example() # call example() and we expect it to throw a ValueError
        