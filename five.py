# Five programming problems
# https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
# 19: 11

from itertools import permutations
numbers = range(5)
# sum of these should be 10

def sum_for():
    # Problem 1
    num_sum = 0
    for each in numbers:
        num_sum += each
    return num_sum

def sum_for_while():
    # Problem 1
    num_sum = 0
    num_len = len(numbers)
    current = 0
    while current < num_len:
        num_sum += numbers[current]
        current += 1
    return num_sum

def sum_for_recursion(numbers):
    # Problem 1
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_for_recursion(numbers[1:])

def combine_lists(l1, l2):
    # Assuming lists are of same length
    result = []
    num_of_elements = len(l1)
    i = 0
    while i < num_of_elements:
        result.append(l1[i])
        result.append(l2[i])
        i += 1
    return result

def fibonacci_numbers(how_many):
    # Problem 3
    first = 0
    second = 1
    result = [first, second]
    computed = 2
    while computed < how_many:
        third = first+second
        result.append(third)
        first, second = second, third
        computed += 1
    return result

def form_largest_number(numbers):
    # Problem 4
    largest = 0
    perms = permutations(numbers)
    def join_integers(num_tuple):
        str_nums = [str(each) for each in num_tuple]
        return "".join(str_nums)
    for each in perms:
        joined_numbers = join_integers(each) 
        joined_numbers_int = int(joined_numbers)
        if joined_numbers_int > largest:
            largest = joined_numbers_int
    return largest

def find_result_100():
    # Problem 5
    # 1,2: [(1, 2), (12)]
    # 1, 2, 3: [(1, 2, 3), (12, 3), (1, 23), (123)]
    # 1, 2, 3, 4: [(1, 2, 3, 4), (12, 3, 4), (1, 23, 4), (1, 2, 34), (123, 4), (12, 34), (1234)]
    #l = range(11)
    pass

assert sum_for() == 10
assert sum_for_while() == 10
assert sum_for_recursion(numbers) == 10
assert combine_lists([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']
assert combine_lists(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
assert fibonacci_numbers(2) == [0, 1]
assert fibonacci_numbers(3) == [0, 1, 1]
assert fibonacci_numbers(4) == [0, 1, 1, 2]
assert fibonacci_numbers(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert form_largest_number([1]) == 1
assert form_largest_number([1, 2]) == 21
assert form_largest_number([1, 3, 2]) == 321
assert form_largest_number([50, 2, 1, 9]) == 95021
find_result_100()