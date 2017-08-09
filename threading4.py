#threading event for signaling

import threading
import time


class Tclass(threading.Thread):
    def __init__(self, name=None, target=None,args=()):
        threading.Thread.__init__(self, name=name, target=target)
        self.args=args
        self.target=target
    def run(self):
        print "starting thread"
        self.target(self.args)
        
def fun1(args):
    print "Function-1 starting"
    args[0].wait()
    print "Function-1 exiting"

def fun2(args):
    print "Function-2 starting"
    time.sleep(10)
    args[0].set()
    print "Function-2 exiting"

def fun3(args):
    print "Function-3 starting"
    while args[0].is_set() == False:
        print "envent not set wait for a sec"
        time.sleep(1)
    print "Function-3 exiting"

e = threading.Event()
T1 = Tclass(name='thread1', target=fun1, args=(e,))
T2 = Tclass(name='thread2', target=fun2, args=(e,))
T3 = Tclass(name='thread3', target=fun3, args=(e,))

T1.start()
T2.start()
T3.start()

T1.join()
T2.join()
T3.join()
print "Main function exiting"
