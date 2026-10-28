import numpy

class HelloWorld:
    def __init__(self):
        self.a = numpy.array([1, 2, 3, 4, 5])
        self.i = numpy.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                             [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])

    def hello_world(self):
        print(self.a[[2,3,4,0,1]])
        print(self.i.shape)
        print(self.i[0, 1, 2])

if __name__ == "__main__":
    hello_world = HelloWorld()
    hello_world.hello_world()