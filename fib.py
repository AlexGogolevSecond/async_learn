
def get_fib(number: int) -> str:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    return f'fib({number}) равно {fib(number)}'
