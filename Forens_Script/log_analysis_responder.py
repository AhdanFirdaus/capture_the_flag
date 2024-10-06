import time
import socket

def connect_and_respond():
    host = '103.145.226.92'
    port = 35353

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        print("Connected to the server.")

        # Wait a moment for the server to send data
        time.sleep(1)

        # Responses to the questions
        responses = [
            "3",                             # Answer for question 1
            "190.253.15.120",                # Answer for question 2
            "bargaintime.jsp",               # Answer for question 3
            "classLoader",                   # Answer for question 4
            "discount_master",               # Answer for question 5
            "15/06/2024:02:24:45",	     # Answer for question 6
            "CVE-2022-22965"          	     # Answer for question 7
        ]

        # Send responses one by one
        for i, response in enumerate(responses, start=1):
            print(f"Answering question {i}: {response}")
            s.sendall((response + '\n').encode('utf-8'))
            time.sleep(1)  # Wait for a moment between responses to avoid overwhelming the server

        # Optional: Receive any final messages from the server
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    connect_and_respond()