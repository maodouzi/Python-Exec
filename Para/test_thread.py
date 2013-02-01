import threading
import time
count = 1

class TestThread(threading.Thread):
	def run(self):
		global count
		print "thread %d: Pretending to do stuff" % count
		count += 1
		time.sleep(2)
		print "down with ststuff %d" % count

for t in range(5):
	TestThread().start()
