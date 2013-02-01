#!/bin/env python
#coding=utf8
#ssh_login.py

import sys
import paramiko

host=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
localpath=sys.argv[4]
filepath=sys.argv[5]

paramiko.util.log_to_file('/tmp/paramiko.log')
port = 22
transport = paramiko.Transport((host, port))

#Next we want to authenticate. We can do this with a password:
transport.connect(username = username, password = password)

#Another way is to use an SSH key:
#import os
#privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
#mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
#username = 'warrior'
#transport.connect(username = username, pkey = mykey)

sftp = paramiko.SFTPClient.from_transport(transport)

#Now lets pull a file across from the remote to the local system:
sftp.get(filepath, localpath)

#Now lets go the other way:
#sftp.put(filepath, localpath)

#Lastly, we need to close the SFTP connection and the transport:
sftp.close()
transport.close()
