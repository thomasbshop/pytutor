# python allows functions to be nested in other functions.
# RECURSION
# A recursive function is a function that calls itself and they can be useful in structures that can contain themselves.
#  e.g. directories in computer file system or computing mathematical functions that are defined recursively.
#  e.g. factorial


def fact(n):
    """ Calculate n! recursively."""
    result = 1
    if n > 1:
        for x in range(2, n+1):
            result *= x

    return result


def factorial(n):
    # n! can also be calculated as n*(n-1)*((n-1)*(n-1)-1) and so on
    """Calculating n! recursively"""
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# recursion doesnt always work for every solution therefore you have to analyse the problem first before using recursive
# techniques. e.g. fibonacci

def fib(n):
    """ F(n) = F(n - 1) + F(n - 2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# def fib(n):
# # write Fibonacci series up to n
# """Print a Fibonacci series up to n."""
# a, b = 0, 1
# while a < n:
# print(a, end=' ')
# a, b = b, a+b
# print()


def fibonacci(n):
    # None recursive. Performs better supprisingly.
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result

    return result


print(factorial(6))

for i in range(0, 120):
    print(i, fibonacci(i))
