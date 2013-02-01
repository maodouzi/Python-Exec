#! /usr/bin/env python
import sys, os, re

IGNORE_FILE_LIST = ["\.svn", "\.swp", "\.git"]
ignoreCmpObj = re.compile("|".join(["(%s)" % item for item in IGNORE_FILE_LIST]))

def myPrint(aObj=""):
	print(str(aObj))

def myExit(errMsg="", errNum=-1):
	if errNum != 0:
		myPrint("Error!")
	myPrint(str(errMsg))
	sys.exit(errNum)

def searchFromFile(filePath, reCmpObj):
	for line in open(filePath):
		line = line.rstrip()
		if reCmpObj.search(line):
			yield "%s: %s" % (filePath, line)

def printFromFile(filePath, reCmpObj):
	matchFlag = False
	for line in searchFromFile(filePath, reCmpObj):
		if not matchFlag:
			myPrint("\n-> Search file: %s" % filePath)
			matchFlag = True
		myPrint(line)

def printFromDir(dirPath, reCmpObj):
	def doDir(arg, dirname, nameList):
		for item in nameList:
			tmpPath = "%s%s%s" % (dirname, os.sep, item)
			if ignoreCmpObj.search(tmpPath):
				continue
			elif os.path.isfile(tmpPath):
				printFromFile(tmpPath, arg)

	os.path.walk(dirPath, doDir, reCmpObj)

if __name__ == "__main__":
	if len(sys.argv) > 4 or len(sys.argv) < 3:
		myExit("Usage: %s <regex> <path> [-i]" % sys.argv[0])
	
	grepPath = sys.argv[2]
	if not os.path.exists(grepPath):
		myExit("grepPath: %s not a valid path!" % grepPath)

	ignoreCase = False
	if len(sys.argv) == 4 and sys.argv[3] == "-i":
		ignoreCase = True

	regexStr = sys.argv[1]
	# myPrint(regexStr)
	try:
		if ignoreCase:
			reCmpObj = re.compile(regexStr, re.I)
		else:
			reCmpObj = re.compile(regexStr)
	except:
		myExit("regexStr: %s not a valid regex!" % regexStr)

	if os.path.isdir(grepPath):
		printFromDir(grepPath, reCmpObj)	
	elif os.path.isfile(grepPath):
		printFromFile(grepPath, reCmpObj)	
