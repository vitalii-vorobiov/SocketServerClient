import socket
import struct
import numpy as np
import cv2

HOST = '192.168.0.240'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Server Started")
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = b""
        while True:
            while len(data) < 4:
                print("Recv: {}".format(len(data)))
                data += conn.recv(4096)

            print("Done Recv: {}".format(len(data)))

            packed_msg_size = data[:4]
            data = data[4:]
            msg_size = struct.unpack("<L", packed_msg_size)[0]

            while len(data) < msg_size:
                data += conn.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            x = np.frombuffer(frame_data, dtype='uint8')
            frame = cv2.imdecode(x, cv2.IMREAD_UNCHANGED)
            cv2.imshow("Test", frame)
            cv2.waitKey(1)
