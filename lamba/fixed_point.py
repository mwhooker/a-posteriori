

def factorial(n):
    """

    >>> factorial(5)
    120
    """
    if n == 1:
        return n
    return n * factorial(n - 1)

lfactorial = lambda n: 1 if n == 0 else n * lfactorial(n - 1)
#print (lambda f: (lambda n: 1 if n == 0 else n * f(n - 1))(f))

#Y = lambda f: f(Y(f))

Y = lambda f: f(lambda x: Y(f)(x))
almost_factorial = lambda f: lambda n: 1 if n == 0 else n * f(n - 1)
factorial = Y(almost_factorial)
print factorial(5)


part_factorial = lambda self, n: 1 if n == 0 else n * self(self, n - 1)
print part_factorial(part_factorial, 5)


part_factorial = lambda self: lambda n: 1 if n == 0 else n * self(self)(n - 1)
factorial = part_factorial(part_factorial)
print factorial(5)

part_factorial = lambda self: lambda n: 1 if n == 0 else n * self(n - 1)(part_factorial)
print part_factorial(5)
