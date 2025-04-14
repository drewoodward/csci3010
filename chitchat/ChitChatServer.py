import socket

def server():
    ip = input("IP to host on (default: localhost): ") or "localhost"
    port_input = input("Port (default: 8080): ")
    port = int(port_input) if port_input else 8080
    server_name = input("Your username: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((ip, port))
        sock.listen(1)
        print(f"Hosting chat on {ip}:{port}... waiting for someone to connect.")

        conn, addr = sock.accept()
        print(f"Connected! From {addr}")

        # Send your username and receive their username
        conn.send(server_name.encode())
        client_name = conn.recv(1024).decode()
        print(f"{client_name} has joined the chat!")

        while True:
            incoming = conn.recv(1024).decode()
            if incoming.strip().lower() == "end":
                print(f"{client_name} left the chat.")
                break
            print(f"{client_name}: {incoming}")

            msg = input(f"{server_name}: ")
            conn.send(msg.encode())

            if msg.strip().lower() == "end":
                print("You ended the chat.")
                break

    except Exception as e:
        print("Error:", e)
    finally:
        try:
            conn.close()
        except:
            pass
        sock.close()

if __name__ == "__main__":
    server()
