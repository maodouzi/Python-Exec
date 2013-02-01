import subprocess

cmdStr = "python test.py %d"

pipeList = []

for i in range(5):
	tmpPipe = subprocess.Popen(cmdStr % i, shell = True, stdout = subprocess.PIPE)
	pipeList.append(tmpPipe)

for i in range(5):
	print pipeList[i].stdout.read()
