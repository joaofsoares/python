# Fibonacci


def fib(num):
    # create help func
    def fibHelper(num, prev, next):
        if (num == 0):
            return prev
        elif num == 1:
            return next
        else:
            return fibHelper(num - 1, next, prev + next)
    # call fib helper passing the initial values
    return fibHelper(num, 0, 1)


# print the result
print(fib(10))
