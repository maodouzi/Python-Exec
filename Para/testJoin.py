import threading
import time

class MyThread(threading.Thread):

      def __init__(self,id):
             threading.Thread.__init__(self)
             self.id=id
      def run(self):
             time.sleep(5)
             print self.id
 
def func():
      #t.setDaemon(True)  # Main thread exit even child thread is live.
      t.start()
      #t.join()	# Main thread block until child thread finished
      print "=" * 5

t=MyThread(2)
func()
