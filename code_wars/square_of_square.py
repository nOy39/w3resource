"""Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.

The tests will always use some integral number,
so don't worry about that in dynamic typed languages."""


def is_square(n):
    from math import sqrt
    return sqrt(n).is_integer() if n >= 0 else False


num = 252

print(is_square(num))
