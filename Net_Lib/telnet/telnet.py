#import getpass
import sys
import telnetlib

HOST = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
cmdStr = sys.argv[4]

#HOST = "localhost"
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

#tn.write("ls\n")
tn.write("%s\n" % cmdStr)
tn.write("exit\n")

print tn.read_all()
