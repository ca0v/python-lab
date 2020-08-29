import sys
import secrets
import string

class MyClass:
    @staticmethod
    def my_fun1(size):
        return ''.join((secrets.choice(string.ascii_letters)) for i in range(size))
    @classmethod
    def my_fun2(self, size):
        return MyClass.my_fun1(size)
    def my_fun3(self, size):
        if size == 1:
            return 1
        elif size == 2:
            return self.my_fun1(4)
        else:
            return self.my_fun1(pow(2,size))

c = MyClass()

def main():
    print(sys.argv)
    print (c.my_fun1 (10))
    print (c.my_fun2 (10))
    print (c.my_fun3 (1))
    print (c.my_fun3 (2))
    print(c.my_fun3(3))
    
main()