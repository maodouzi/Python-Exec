import threading
import time, sys, os

class myThread(threading.Thread):

    def __init__(self, threadname, waitTime):
        threading.Thread.__init__(self,name=threadname)
        self.waitTime = waitTime
    def run(self):
        time.sleep(self.waitTime)
        print self.getName()

def fun1():
    t1.start()
    print 'fun1 done'

def fun2():
    t2.start()
    print 'fun2 done'

t1=myThread('t1', 2)
t2=myThread('t2', 3)
t1.setDaemon(False)
t2.setDaemon(True)
fun1()
fun2()

#both exit will make script exit right now!
#sys.exit()
#os._exit(0)
