#! /usr/bin/env python
import sys, os, re

USELESS_FILE_LIST = ["^Thumbs\.db$", "~$", "\.swp$", "\.bak$", "\.pyc$"]
uselessCmpObj = re.compile("|".join(["(%s)" % item for item in USELESS_FILE_LIST]))

def myPrint(aObj):
	print(str(aObj))

def myExit(errMsg="", errNum=-1):
	if errNum != 0:
		myPrint("Error!")
	myPrint(str(errMsg))
	sys.exit(errNum)

if __name__ == "__main__":
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		myExit("Usage: %s <dir path> [-d]" % sys.argv[0])

	findPath = sys.argv[1]
	if not os.path.isdir(findPath):
		myExit("findPath: %s not a valid dir!" % findPath)

	rmFlag = False
	if len(sys.argv) == 3 and sys.argv[2] == "-d":
		rmFlag = True
	
	# findPath = os.path.abspath(findPath)

	def doDir(arg, dirname, nameList):
		for item in nameList:
			tmpPath = "%s%s%s" % (dirname, os.sep, item)
			if os.path.isfile(tmpPath) and uselessCmpObj.search(item):
				myPrint(tmpPath)
				if rmFlag:
					os.remove(tmpPath)

	os.path.walk(findPath, doDir, "")
