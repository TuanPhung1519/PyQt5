import os, sys
modules_path = os.path.abspath(os.path.join("modules"))
sys.path.append(modules_path)
print(sys.path)


from sub1 import subprogram1
from sub2 import subprogram2
from sub3 import subprogram3

class mainprogram():
    def __init__(self):
        print("This is init main!")
    def submain(self):
        a = subprogram1()
        b = subprogram2()
        c = subprogram3()
        a.funcsub1()
        b.funcsub2()
        c.funcsub3()
if __name__ == '__main__':
    main = mainprogram()
    main.submain()
