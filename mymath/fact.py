num = 0

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

def increment():
    global num
    num = num + 1