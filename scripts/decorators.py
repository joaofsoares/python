'''
Decorators
'''


def old_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")
    return wrap_func


def original_func():
    print("Using decorator")


decorated_func = old_decorator(original_func)
decorated_func()


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")
    return wrap_func


@new_decorator
def new_original_func():
    print("Using decorator annotation")


new_original_func()
