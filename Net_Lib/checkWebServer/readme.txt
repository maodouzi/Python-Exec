1. 连接失败
>python checkWebServer.py -a 192.168.211.129
options: {'resource': 'index.html', 'port': 80, 'address': '192.168.211.129'}, a
rgs: []
HTTP connection created successfully
HTTP connection failed: (10061, 'Connection refused')
HTTP connection closed successfully
check_webserver returned False

2. 连接到webserver，但是网页不存在 
>python checkWebServer.py -a 192.168.211.129 -p 8080
options: {'resource': 'index.html', 'port': 8080, 'address': '192.168.211.129'},
 args: []
HTTP connection created successfully
request for /index.html successful
response status: 404
HTTP connection closed successfully
check_webserver returned False

3. 网页存在
>python checkWebServer.py -a 192.168.211.129 -p 8080 -r ""
options: {'resource': '', 'port': 8080, 'address': '192.168.211.129'}, args: []
HTTP connection created successfully
request for / successful
response status: 200
HTTP connection closed successfully
check_webserver returned True