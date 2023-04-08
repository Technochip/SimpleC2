import socket

X = input("Enter the IP address: ")
Y = int(input("Enter the port: "))
Z = input("Enter the data to send: ")

s = socket.socket()

try:
    s.connect((X, Y))
except socket.error as e:
    print("Error connecting to server:", e)
    s.close()
    exit()

try:
    s.send(Z.encode())
except socket.error as e:
    print("Error sending data:", e)
finally:
    s.close()

