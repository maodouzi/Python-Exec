1. Test SSHD
>python testPortBySocket.py -a 192.168.211.129 -p 22
options: {'port': 22, 'address': '192.168.211.129'}, args: []
Attempting to connect to 192.168.211.129 on port 22
Connected to 192.168.211.129 on port 22
check_server returned True

2. test Telnetd
>python testPortBySocket.py -a 192.168.211.129 -p 23
options: {'port': 23, 'address': '192.168.211.129'}, args: []
Attempting to connect to 192.168.211.129 on port 23
Connection to 192.168.211.129 on port 23 failed: (10061, 'Connection refused')
check_server returned False