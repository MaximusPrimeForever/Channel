import socket

print("Channel ver." + "1.0")
print("Listen or Connect?")
usr_inp = 0
port = 5984

while usr_inp == 0:
    try:
        usr_inp = int(input("1. Listen\n2. Connect\n"))
    except ValueError:
        print("Bad input")

if usr_inp == 1:
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    conn.bind((host, port))

    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            break

        print(recv_msg)
        msg = input("> ")
        conn.sendto(msg)
    conn.close()

else:
    # peer = input("Peer IP: ")
    peer = socket.gethostname()
    conn = socket.socket()
    conn.connect((peer, port))

    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            break

        print(recv_msg)
        msg = input("> ")
        conn.sendto(msg)
    conn.close()