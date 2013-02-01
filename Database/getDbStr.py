'''
Created on 2011-1-6

@author: wenxianw
'''

import MySQLdb, sys

def getDatasFromDB(queryStr):
    print queryStr
    db = MySQLdb.connect(user='root', db='brainpower', passwd='123', host='localhost')
    cursor = db.cursor()
    cursor.execute(queryStr)
    returnDatas = [row for row in cursor.fetchall()]
    db.close()
    return returnDatas

def getRevData():
    queryReturn = getDatasFromDB('select * from rev_rawmsg')
    return queryReturn

def truncateRev():
    getDatasFromDB('truncate table rev_rawmsg')
    getDatasFromDB('truncate table send_rawmsg')

if __name__ == '__main__':
    print getRevData()
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        truncateRev()
    
