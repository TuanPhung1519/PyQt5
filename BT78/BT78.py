import os
from multiprocessing import Process, current_process

#Ham chay tren tung process=> Ta cho cac process cung chay 1 ham
def square(number):
    result = number*number
    #Get id of Process
    #process_id = os.getpid()
    #print(f"Process ID: {process_id}")
    print(f"Process name: {current_process().name}")
    print(f"The number {number} square to {result}")

if __name__ == '__main__':
    #Khai bao mang quan ly process
    processes = []
    numbers = [1,2,3,4]
    for number in numbers:
        process = Process(target=square, args=(number,))
        #Them vao mang de quan ly
        processes.append(process)
        process.start()