class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        raise NotImplementedError("Subclass must implement this method")

    def __str__(self):
        return f'I am an animal called {self.name}'
