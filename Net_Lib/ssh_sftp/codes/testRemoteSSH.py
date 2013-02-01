#!/bin/env python
#coding=utf8
#ssh_login.py

import sys
import paramiko

host=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
command=sys.argv[4]

ssh_con=paramiko.SSHClient()
ssh_con.load_system_host_keys()
ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
         ssh_con.connect(hostname=host,username=username,password=password)
except paramiko.AuthenticationException:
         print "Auth Failed!"
         sys.exit(1)
except socket.error:
         print "Server is unreachable!"
         sys.exit(2)
else:
         stdin,stdout,stderr=ssh_con.exec_command(command)
         print stdout.read()
         ssh_con.close()
