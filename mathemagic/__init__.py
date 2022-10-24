'''
MATHEMAGIC - Module containing a lot of general and commonly used mathematical functions.

Visit Our Official Repository For More Info: https://github.com/FireHead90544/mathemagic
Author: Rudransh Joshi (https://github.com/FireHead90544)

This module is licensed under GNU GPL v3, check LICENSE for more info about LICENSE.

                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.
'''


import math
import random

def factorial(num: int):
    '''
    Returns: Factorial of a number.
    Arguments - num: int
    Must be less than 10,000 else it would be too much for CPU to calculate.
    '''
    if num < 0:
        return Exception("NegationError: Factorials of negative numbers don't exists.")
    elif num == 0:
        return 1
    elif num > 10000:
        return Exception("OverflowError: That is too much to calculate, also no need of that much big factorial.")
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial


def pi(digits: int = 2):
    '''
    Returns: The value of pi till digits given after float.
    Arguments - digits: int
    '''
    digits = abs(digits)
    if digits <= 2:
        digits = 3
    digits = digits + 2
    return float(str(math.pi)[0:digits])


def random(x: int, y: int):
    '''
    Returns: A random number between x and y.
    Arguments - x: int, y: int
    '''
    return random.randint(x, y)


def odd(num: int):
    '''
    Returns: True if num is odd else returns False.
    Arguments - num: int
    '''
    if num % 2 != 0:
        return True
    else:
        return False


def even(num: int):
    '''
    Returns: True if num is even else returns False.
    Arguments - num: int
    '''
    if num % 2 == 0:
        return True
    else:
        return False


def numType(num: int):
    '''
    Returns: "Even" if num is even, else "Odd" is num is odd.
    Arguments - num: int
    '''
    if num % 2 == 0:
        return "Even"
    elif num % 2 != 0:
        return "Odd"


def prime(num: int):
    '''
    Returns: True if num is prime, else returns False.
    Arguments - num: int
    '''
    if num <= 1:
      return False
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i) == 0: 
            return False
    return True

def hcf(x: int, y: int):
    '''
    Returns: HCF / GCD of the x and y.
    Arguments - x: int, y: int
    '''
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf


def gcd(x: int, y: int):
    '''
    Returns: HCF / GCD of the x and y.
    Arguments - x: int, y: int
    '''
    return hcf(x, y)


def armstrong(num: int):
    '''
    Returns: True if a number is armstrong number, else returns False.
    Arguments - num: int
    '''
    num = str(num)
    cubes = []
    for item in num:
        item = int(item) ** 3
        cubes.append(item)

    if sum(cubes) == int(num):
        return True
    else:
        return False


def square(num: float):
    '''
    Returns: Square of the num.
    Arguments - num: int
    '''
    return num ** 2


def cube(num: float):
    '''
    Returns: Cube of the num.
    Arguments - num: int
    '''
    return num ** 3


def palindrome(num: int):
    '''
    Returns: True if the num is palindrome, else returns False
    Arguments - num: int
    '''
    if num == int(str(num)[::-1]):
        return True
    else:
        return False


def power(num: int, pow: int):
    '''
    Returns: num raise to pow
    Arguments - num: int, pow: int
    '''
    return num ** pow


def fibonacci(terms: int):
    '''
    Returns: List of elements of members in fibonacci series.
    Arguments - terms: int
    '''
    n1, n2 = 0, 1
    count = 0
    fibonacci_series = []
    while count < terms:
        fibonacci_series.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return fibonacci_series


def calculate(expression: str):
    '''
    Returns: Answer of the expression, if can successfully evaluate, else returns EvaulationError.
    Arguments - terms: int
    '''
    try:
        return eval(expression)
    except Exception:
        return Exception("EvaluationError: Unable to evaluate the given expression, are you using correct operations?")


__version__ = '1.1'
