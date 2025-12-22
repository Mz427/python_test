import hello_world

class Test01:
    def __init__(self):
        self.name = __name__
        self.name_file = "test01.py"

    def print_name(self):
        print(f"The {self.name_file}'s __name__ is {self.name}")

if __name__ == "__main__":
    test = Test01()
    test.print_name()
    
    hello = hello_world.HelloWorld()
    hello.print_name()