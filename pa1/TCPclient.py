from socket import *

server_ip = "localhost"
server_port = 8000

client_name = "andre-client"

# Get and validate user input
while True:
    client_number_str = input("Please enter a number between 1 and 100: ")
    try:
        client_number = int(client_number_str)
        if 1 <= client_number <= 100:
            break
        else:
            print("Error: The number must be between 1 and 100. Try again.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Compose message: "<client_name> <client_number>"
client_message = client_name + " " + str(client_number)

# Create client socket (IPv4, TCP)
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect client with server
client_socket.connect((server_ip, server_port))
print(f"Connected to server at {server_ip}:{server_port}")

# Send message to the server
client_socket.send(client_message.encode())
print(f"Sent message to server: {client_message}")

# Receive message from server (expected format: "andre-server <server_number>")
server_message = client_socket.recv(2048).decode()
print(f"Received message from server: {server_message}")

# Parse the server's response
parts = server_message.split(" ")
if len(parts) >= 2:
    server_name = parts[0]
    try:
        server_number = int(parts[1])
    except ValueError:
        print("Error: Server number is not valid.")
        server_number = 0
else:
    print("Error: Received message in unexpected format.")
    server_name = "unknown"
    server_number = 0

# Compute the sum of the client's number and the server's number
total = client_number + server_number

# Display final details
print("\n--- Final Results ---")
print(f"Client Name: {client_name}")
print(f"Client's Number: {client_number}")
print(f"Server Name: {server_name}")
print(f"Server's Number: {server_number}")
print(f"Sum: {total}")

# Close client socket
client_socket.close()
print("Client socket closed.")
