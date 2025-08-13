import socket
import select

class SequentialMultiPortServer:
    def __init__(self, ports, host='0.0.0.0'):
        self.host = host
        self.ports = ports
        self.server_sockets = []

    def setup_sockets(self):
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.host, port))
            s.listen(1)  # Only one client at a time per port
            s.setblocking(False)  # So we can poll multiple sockets
            self.server_sockets.append(s)
            print(f"[+] Listening on port {port}")

    def start(self):
        self.setup_sockets()
        try:
            while True:
                # Wait for any socket to become ready
                ready_sockets, _, _ = select.select(self.server_sockets, [], [])

                for s in ready_sockets:
                    conn, addr = s.accept()
                    port = s.getsockname()[1]
                    print(f"[Port {port}] Connected by {addr}")
                    self.handle_client(conn, addr, port)
        except KeyboardInterrupt:
            print("\n[!] Server shutting down.")
        finally:
            for s in self.server_sockets:
                s.close()

    def handle_client(self, conn, addr, port):
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"[Port {port}] Client {addr} disconnected")
                    break
                print(f"[Port {port}] Received: {data}")
                conn.sendall(data)  # Echo

if __name__ == "__main__":
    ports = [12345, 12346, 12347]  # Add any ports you want
    server = SequentialMultiPortServer(ports)
    server.start()
