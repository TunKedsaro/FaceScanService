from fastapi import FastAPI, File, UploadFile, HTTPException
import socket
import numpy as np
import cv2

app = FastAPI()
@app.post("/api/v3/facescan/upload")
# async def add_numbers(num1:float, num2:float):
async def create_upload_file(
    file : UploadFile = File(...)
):
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
        ## Got image then -> Get size
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # img_shape = image.shape
        w,h,c = image.shape

        # 05 Communicaiton mode
        message = f"{w},{h},{c}"

        encode_message = message.encode()
        client_socket.sendall(encode_message)
        
        # Receive the result
        result = client_socket.recv(1024).decode()
        client_socket.close()
        # result = float(result)
        # return {"result":result}
        h, w, c = map(float, result.split(","))
        return {"result": 
                {"height": h, "width": w, "channels": c}
            }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))