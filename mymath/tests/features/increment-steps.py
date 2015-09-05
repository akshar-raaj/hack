from lettuce import *
from fact import num, increment

@step('I have access to increment')
def access(step):
    pass

@step('I use increment')
def use_increment(step):
    increment()

@step('num is (\d+)')
def num_is(step, number):
    number = int(number)
    assert num == number, "Expected %d, found %d" % (number, num)