'''
Created on 2010-12-29

@author: wenxianw
'''

from printFun import printMode

def createPrinter(mode = "text"):
    def defFun():
        print "No such mode: %s!" % mode 
        
    fun = getattr(printMode, "print_%s" % mode, "")
    if fun != "":
        return fun
    else:
        return defFun

if __name__ == '__main__':
    printer = createPrinter("text")
    printer()
    printer = createPrinter("dddd")
    printer()
        