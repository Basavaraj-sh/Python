#sub threading for passing args to the target function

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
    print args
    print "mul:{0}".format(int(args[0]) * int(args[1]))
    time.sleep(3)
    print "Function-1 exiting"

def fun2(args):
    print "Function-2 starting"
    print args
    print "add:{0}".format(int(args[0]) + int(args[1]))
    time.sleep(3)
    print "Function-2 exiting"

T1 = Tclass(name='thread1', target=fun1, args=(2,8))
T1.setDaemon(True)
T2 = Tclass(name='thread2', target=fun2, args=(5,8))
T2.setDaemon(True)

T1.start()
T2.start()

T1.join()
T2.join()
print "Main function exiting"
