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
    cap = cv2.VideoCapture(0)
    conn, addr = s.accept()
    with conn:
        while True:
            ret, frame = cap.read()
            print(frame)
            break