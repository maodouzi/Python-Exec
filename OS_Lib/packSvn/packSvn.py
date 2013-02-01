#! /usr/bin/env python
import shutil, sys, os, tarfile, datetime
from contextlib import closing

def myPrint(aObj):
	print(str(aObj))

def myExit(errMsg="", errNum=-1):
	if errNum != 0:
		myPrint("Error!")
	myPrint(str(errMsg))
	sys.exit(errNum)

SVN_DIR_NAME = "svn-local_%s_tar"
SVN_TAR_NAME = "svn-local_%s_%s.tar.gz"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		myExit("Usage: %s <src> <dst>" % sys.argv[0])	

	myPrint("Begin Packing SVN\n")
	srcPath = sys.argv[1]
	if not os.path.isdir(srcPath):
		myExit("src: %s not a valid dir!" % srcPath)
	dstPath = sys.argv[2]
	if not os.path.isdir(dstPath):
		myExit("dst: %s not a valid dir!" % dstPath)

	srcPath = os.path.abspath(srcPath)
	dstPath = os.path.abspath(dstPath)

	if dstPath.find(srcPath) != -1:
		myExit("dst(%s) in src(%s)" % (dstPath, srcPath))

	dstSvnPath = "%s%s%s" % (dstPath, os.sep, (SVN_DIR_NAME % os.path.basename(srcPath)))
	dstTarPath = "%s%s%s" % (dstPath, os.sep, (SVN_TAR_NAME % (os.path.basename(srcPath), datetime.date.today())))

	if os.path.exists(dstSvnPath):
		shutil.rmtree(dstSvnPath)
		
	def callback(src, name):
		#myPrint(src)
		#myPrint(name)
		return [".svn", ".git"] 
	shutil.copytree(srcPath, dstSvnPath, ignore=callback)

	os.chdir(dstPath)
	with closing(tarfile.open(dstTarPath, mode="w:gz")) as tarOut: 
		tarOut.add(SVN_DIR_NAME % os.path.basename(srcPath))

	try:
		if tarfile.is_tarfile(dstTarPath):
			myPrint("%s tar finished!\n" % dstTarPath)
	except IOError, err:
		myPrint("%s\t%s" % (dstTarPath, err))

	with closing(tarfile.open(dstTarPath, mode="r:gz")) as tarIn: 
		for item in  tarIn.getnames():
			myPrint(item)
	"""
	def targz(arg, dirname, name):
		myPrint("%s->%s" % (dirname, name))

	os.path.walk(dstSvnPath, targz, "")
	"""
	myPrint("\nEnd Packing SVN")
