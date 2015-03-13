def is_prime(num):
    assert num > 1
    if num == 2:
        return True
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True

def primes_greater_than_equal_num(num):
    while True:
        if is_prime(num):
            yield num
        num = num + 1