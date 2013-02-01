#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue
num_threads = 3
queue = Queue()
def pinger(i, q):
	"""Pings subnet"""
	while True:
		count = q.get()
		print "Thread %d: Count= %d" % (i, count)
		ret = subprocess.call("python test.py %d" % count, shell=True)
		if ret == 0:
			print "%d => %d: run successful!" % (i, count)
		else:
			print "%d => %d: did not respond" % (i, count)
		q.task_done()

for i in range(num_threads):
	worker = Thread(target=pinger, args=(i, queue))
	worker.setDaemon(True)
	worker.start()

for count in range(5):
	queue.put(count)

print "Main Thread Waiting"
queue.join()
print "Done"
