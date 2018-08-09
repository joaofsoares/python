'''
Generators
'''


def create_cubes(n):
    for x in range(n):
        yield x ** 3


gen = create_cubes(10)
print(next(gen))
