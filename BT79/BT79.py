import os

from multiprocessing import Value, Process

def add(total):
    total.value = 12
    print("Process 1: ", total.value)



def sub(total):
    total.value -= 5
    print("Process 2: ", total.value)

if __name__ == '__main__':
    total = Value('i', 500)
    process1 = Process(target=add, args=(total,))
    process2 = Process(target=sub, args=(total,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()



