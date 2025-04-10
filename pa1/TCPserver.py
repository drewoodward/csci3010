from socket import *
import random

server_ip = "localhost"
server_port = 8000

server_name = "andre-server"

# Create server socket (IPv4, TCP)
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind server socket to IP and port
server_socket.bind((server_ip, server_port))
print(f"Server started on {server_ip}:{server_port}")

# Set server to listen for incoming connections (queue length 1)
server_socket.listen(1)
print("Server is listening for connections...")

while True:
    # Accept incoming client connection request
    connection_socket, client_address = server_socket.accept()
    print(f"\nConnection accepted from {client_address}")

    # Receive message from client
    client_message = connection_socket.recv(2048).decode()
    print(f"Received message from client: {client_message}")

    # Split the message into the client's name and number
    parts = client_message.split(" ")
    if len(parts) >= 2:
        client_name = parts[0]
        try:
            client_number = int(parts[1])
        except ValueError:
            print("Error: Client number is invalid.")
            connection_socket.close()
            continue
    else:
        print("Error: Received message in an unexpected format.")
        connection_socket.close()
        continue

    # Print client and server names
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")

    # Server randomly picks an integer between 1 and 100
    server_number = random.randint(1, 100)

    # Compute the sum of the client's number and the server's number
    total = client_number + server_number
    print(f"Client's Number: {client_number}")
    print(f"Server's Number: {server_number}")
    print(f"Sum: {total}")

    # Prepare server response: "andre-server <server_number>"
    server_message = server_name + " " + str(server_number)

    # Send response to the client
    connection_socket.send(server_message.encode())
    print("Sent response to client.")

    # Close the connection socket
    connection_socket.close()
    print("Closed connection with client.")
