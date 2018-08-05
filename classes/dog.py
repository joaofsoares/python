from classes.animal import Animal


class Dog(Animal):
    def eat(self):
        print(f'My name is {self.name} and I like bones')

    def __str__(self):
        return f'I am a dog called {self.name}'
