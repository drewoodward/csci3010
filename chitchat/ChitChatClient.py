import socket

def client():
    ip = input("Server IP (default: localhost): ") or "localhost"
    port_input = input("Port (default: 8080): ")
    port = int(port_input) if port_input else 8080
    client_name = input("Your username: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
        print("Connected to server")

        # Receive server name and send your own name
        server_name = s.recv(1024).decode()
        s.send(client_name.encode())

        print(f"You are now chatting with {server_name}!")

        while True:
            msg = input(f"{client_name}: ")
            s.send(msg.encode())

            if msg.strip().lower() == "end":
                print("You left the chat.")
                break

            reply = s.recv(1024).decode()
            if reply.strip().lower() == "end":
                print(f"{server_name} ended the chat.")
                break

            print(f"{server_name}: {reply}")

    except Exception as e:
        print("Something broke:", e)
    finally:
        s.close()

if __name__ == "__main__":
    client()
