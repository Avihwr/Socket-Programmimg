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


        if not data1:
            # if data is not received break
            break
        num1 = int(data1)
        num2 = int(data2)

        A = float(num1/num2)
        final = str(A)

        # data = input(' -> ')
        conn.send(final.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
