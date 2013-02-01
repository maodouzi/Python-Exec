'''
Created on 2010-12-30

@author: wenxianw
'''

class Singleton(object):
    class __OnlyOne: 
        def __init__(self): 
            pass

        def __str__(self): 
            return 'Non'

    instance = {} 
    def __init__(self): 
        if self.__class__ not in Singleton.instance:
            Singleton.instance[self.__class__] = Singleton.__OnlyOne()
        else :
            print 'warning : trying to recreate a singleton'

    def __getattr__(self, name): 
        return getattr(self.instance[self.__class__], name)

    def __setattr__(self, name, value):
        return setattr(self.instance[self.__class__], name, value)

if __name__ == '__main__':
    singleton = Singleton()
    singleton.arg1 = "haha"
    
    singleton2 = Singleton()
    print singleton2.arg1