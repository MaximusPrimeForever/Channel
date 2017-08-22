import socket

print("Channel ver." + "1.0")
print("Listen or Connect?")
usr_inp = 0
m_port = 5984
m_input_str = "> "

while usr_inp == 0:
    try:
        usr_inp = int(input("1. Listen\n2. Connect\n"))
    except ValueError:
        print("Bad input")

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if usr_inp == 1:
    # listen
    conn.bind(('', m_port))
    conn.listen(1)

    conn, addr = conn.accept()
    print('Connection address:', addr)
    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            break

        print(recv_msg.decode())
        msg = input(m_input_str)
        conn.send(msg.encode())
    conn.close()

else:
    # connect
    peer = input("Peer IP: ")
    msg = input(m_input_str)

    conn.connect((peer, m_port))
    conn.send(msg.encode())
    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            break

        print(recv_msg.decode())
        msg = input(m_input_str)
        conn.send(msg.encode())
    conn.close()
