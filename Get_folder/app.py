from fastapi import FastAPI, HTTPException
import socket

app = FastAPI()
@app.post("/api/v3/facescan/upload")
async def add_numbers(num1:float, num2:float):
    try:
        # 01 Initial/Unbound mode
        client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        # 02 Bound Mode
        client_socket.connect(
            ("FaceInputAuth_service",8081)
        )
        # 05 Communicaiton mode
        message = f"{num1},{num2}"
        encode_message = message.encode()
        client_socket.sendall(encode_message)
        # Receive the result
        result = client_socket.recv(1024).decode()
        client_socket.close()
        result = float(result)
        return {"result":result}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))