import socket

X = input("Enter the IP address: ")
Y = int(input("Enter the port: "))
Z = input("Enter the payload to send: ")

s = socket.socket()

try:
    s.connect((X, Y))
except socket.error as e:
    print("Error connecting to server:", e)
    s.close()
    exit()

try:
    s.send(Z.encode())
    print("Sending successful!")
except socket.error as e:
    print("Sending failed:", e)
finally:
    s.close()


