# This code lives in module.py
#
# Simple example of a Python module that exports functions
# to be used by other modules.
# 
# A possible use case is to package up a bunch of functions
# which are often used by your scripts.
#
# Inside your scripts you presumably have written
#
# import module

def doubler(x):
    return x * 2

# What follows is a straightforward testing capability for this
# function. We notice that __name__ is set to "__main__" when we
# *run* this script, but it's set to the name of this module when
# we import the module.

if __name__ == '__main__':
    # We ran this script, rather than importing it
    print('Running unit tests...')
    assert doubler(2) == 4
    assert doubler('two') == 'twotwo'
    print('All tests passed!')