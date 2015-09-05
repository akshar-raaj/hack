from lettuce import *

from fact import factorial

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)

@step('I compute the factorial')
def compute_factorial(step):
    world.number = factorial(world.number)

@step('I see the result (\d)')
def see_result(step, result):
    result = int(result)
    assert world.number == result
    assert world.name == 'akshar'
