#! /usr/bin/env python
import sys, os, re

IGNORE_FILE_LIST = ["\.svn", "\.git"]
ignoreCmpObj = re.compile("|".join(["(%s)" % item for item in IGNORE_FILE_LIST]))

def myPrint(aObj):
	print(str(aObj))

def myExit(errMsg="", errNum=-1):
	if errNum != 0:
		myPrint("Error!")
	myPrint(str(errMsg))
	sys.exit(errNum)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		myExit("Usage: %s <dir path>" % sys.argv[0])

	findPath = sys.argv[1]
	if not os.path.isdir(findPath):
		myExit("findPath: %s not a valid dir!" % findPath)
	
	# findPath = os.path.abspath(findPath)

	def printDir(arg, dirname, nameList):
		if ignoreCmpObj.search("%s%s" % (dirname, os.sep)):
			return
		myPrint("%s%s" % (dirname, os.sep))
		for item in nameList:
			tmpPath = "%s%s%s" % (dirname, os.sep, item)
			if not os.path.isdir(tmpPath):
				myPrint(tmpPath)

	os.path.walk(findPath, printDir, "")
