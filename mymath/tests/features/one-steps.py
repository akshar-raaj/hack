from fact import factorial

from lettuce import *

@step('I compute the factorial of (\d+)')
def compute_factorial(step, number):
    number = int(number)
    world.result = factorial(number)

@step('The result is (\d+)')
def result(step, expected):
    assert int(expected) == world.result
