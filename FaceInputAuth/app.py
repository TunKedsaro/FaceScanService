import socket

def start_server():
    # 01 Initail/Unbound mode
    server_socket = socket.socket(
        socket.AF_INET,                                    # AF_INET -> IPV4, It's mean IPV4 gonna communication with something like 192.168.1.1
        socket.SOCK_STREAM                                 # Create communication between Socket
        )
    # 02 Bound mode
    host = "0.0.0.0"                                       # Local host
    port = 8081                                            # Port

    server_socket.bind(                                    # การทำให้เป็นตัวรับหรือตัวส่ง จาก Port และ Address นั้น
        (host, port)                                       # หลังจากการ bind แล้วมันจะสามารเริ่ม Listen ได้
        )
    # 03 Listen mode
    server_socket.listen(5)
    print("Plus service is listening on port 8081...")
    
    while True:
        # 04 Accepting mode
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        # 05 Communication mode
        # Debugging: Print received data
        data = client_socket.recv(1024).decode()
        print(f"Received data: {data}")  # Debugging line
        
        # Parse and process the data
        num1, num2 = map(float, data.split(","))
        result = num1 + num2
        # 06 Close mode
        client_socket.sendall(str(result).encode())
        client_socket.close()


if __name__ == "__main__":
    start_server()
