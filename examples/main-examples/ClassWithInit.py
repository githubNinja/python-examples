class ClassWithInit:

    def __init__(self, arg1):
        self.arg1 = arg1
        print(f"arg::{arg1}")

    def funct1(self):
        print("hello from Func1:")

    def returnNum(self):
        print(f"Arg1:::{self.arg1}")
        return self.arg1

instance = ClassWithInit(12)
instance.returnNum()
