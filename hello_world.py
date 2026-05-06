import numpy

class HelloWorld:
    def __init__(self):
        self.i = numpy.array([[['a', 'b', 'c'], ['d', 'e', 'f']],
                              [['g', 'h', 'i'], ['j', 'k', 'l']]])

    def hello_world(self):
        x, y, z = 1, 0, 2
        print(x, y, z)
        print(self.i[x, y, z])

if __name__ == "__main__":
    hello_world = HelloWorld()
    hello_world.hello_world()