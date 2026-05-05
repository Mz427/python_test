import numpy

class HelloWorld:
    def __init__(self, i):
        self.i = i

    def say_hello_world(self):
        print(self.i[::-1])
        print(self.i)

if __name__ == "__main__":
    hello_world = HelloWorld([1, 2, 3, 4, 5])
    hello_world.say_hello_world()