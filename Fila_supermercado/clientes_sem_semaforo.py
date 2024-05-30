import threading
import time

def cliente1():
    print('Cliente 1 sendo atendido')
    time.sleep(8)
    print('Cliente 1 atendido!')
    time.sleep(.5)
    
def cliente2():
    print('Cliente 2 sendo atendido')
    time.sleep(4)
    print('Cliente 2 atendido!')
    time.sleep(.5)

def cliente3():
    print('Cliente 3 sendo atendido')
    time.sleep(6)
    print('Cliente 3 atendido!')
    time.sleep(.5)

def cliente4():
    print('Cliente 4 sendo atendido')
    time.sleep(2)
    print('Cliente 4 atendido!')
    time.sleep(.5)

t1 = threading.Thread(target=cliente1).start()
t2 = threading.Thread(target=cliente2).start()
t3 = threading.Thread(target=cliente3).start()
t4 = threading.Thread(target=cliente4).start()