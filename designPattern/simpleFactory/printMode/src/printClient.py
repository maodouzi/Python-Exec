'''
Created on 2010-12-29

@author: wenxianw
'''

from printFactory import createPrinter

if __name__ == '__main__':
    printer = createPrinter("text")
    printer()
    printer = createPrinter("pdf")
    printer()
    printer = createPrinter("xxx")
    printer()