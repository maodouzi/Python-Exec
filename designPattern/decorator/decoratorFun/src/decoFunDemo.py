'''
Created on 2010-12-30

@author: wenxianw
'''

def decoFun(func):
    def replaceFunc():
        print "Enter decorator"
        return func()
    return replaceFunc

def myFun():
    print "Enter MyFunc"

if __name__ == '__main__':
    # The original function
    myFun()
    
    # Decorated, then call
    decoFun(myFun)()
    
    # Decorated, call with the same name
    tmpFun = myFun
    @decoFun
    def myFun():
        tmpFun()
    myFun()