import sys

class A():
    def __init__(self):
        super().__init__()
        #1. Class A->B
        #r = B(index1=[1,2])
        self.send()
    def send(self):
        #2. def Class A ->B
        data = [4,5]
        b = B()
        b.receive(index2=data)





class B():
    def __init__(self):
        super().__init__()
        # 1. Class A->B
        '''self.a = index1
        print("Class A->B=", self.a)'''
        # 2. def Class A ->B
        '''a = index1
        print("Class A->B=", a)'''



    def receive(self, index2=0):
        '''b = self.a
        print("A:",b)'''

        c = index2
        print("def A -> def B=",c)


if __name__ == '__main__':
    A()