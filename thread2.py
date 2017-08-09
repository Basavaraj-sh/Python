import threading
import time
def fun1():
    print "Function-1 starting"
    time.sleep(3)
    print "Function-1 exiting"

def fun2():
    print "Function-2 starting"
    time.sleep(3)
    print "Function-2 exiting"

T1 = threading.Thread(name='thread1', target=fun1)
T1.setDaemon(True)
T2 = threading.Thread(name='thread2', target=fun2)
T2.setDaemon(True)

T1.start()
T2.start()

T1.join()
T2.join()
print "Main function exiting"
