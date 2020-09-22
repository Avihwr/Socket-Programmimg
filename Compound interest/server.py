import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data1 = conn.recv(1024).decode()
        data2 = conn.recv(1024).decode()
        data3 = conn.recv(1024).decode()
        data4 = conn.recv(1024).decode()

        if not data1:
            # if data is not received break
            break
        As = str(data1)
        Ps = str(data2)
        rs = str(data3)
        ns = str(data4)

        P = float(As)
        r = float(Ps)
        n = float(rs)
        t = float(ns)

        J = (1 + r/n)**(n*t)
        A = P*J
        final = str(A)

        # data = input(' -> ')
        conn.send(final.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
