
def caching_fibonacci() -> function:
    """This returns function to find fibonacci number!"""
    cache = {}
    def fibonacci(n: int) -> int:
        """This returns a fibonacci number by it's count."""
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))
