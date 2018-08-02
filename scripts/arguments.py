def my_args_func(*args):
    return sum(args)


print(my_args_func(1, 2, 3, 4))


def my_kwargs_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


my_kwargs_func(fruit='apple', veggie='lettuce')


def my_full_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_full_func(1, 2, 3, fruit='banana', food='bacon')
