import socket
ip = "192.168.56.1"
s = socket.socket(2, 1) #socket.AF_INET, socket.SOCK_STREAM

def porttry(ip, port):
    try:
        s.connect((ip, port))
        return True
    except:
        return None

for port in range(0, 10000):
    value = porttry(ip, port)
    if value == None:
        print("Port not opened on %d" % port)
    else:
        print("Port opened on %d" % port)
        break
raw_input()