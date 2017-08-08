import thread
import time
def print_thread(thread_name, time):
    print ("Thread:{0}".format(thread_name))

print ("create threads")
try:
    thread.start_new_thread(print_thread, ("Thread_1", 1))
    thread.start_new_thread(print_thread, ("Thread_2", 2))
except Exception as e:
    print e

print(dir(thread))
#time.sleep(1)
print "End"
