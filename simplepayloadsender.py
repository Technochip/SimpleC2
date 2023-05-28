import socket


X = input("Enter the IP address: ")
Y = int(input("Enter the port: "))

s = socket.socket()

try:
    s.connect((X, Y))
except socket.error as e:
    print("Error connecting to listner:", e)
    s.close()
    exit()

while True:
    Z = input("Enter the payload to send (type 'exit' to quit): ")
    if Z.lower() == 'exit':
        break

    try:
        s.send(Z.encode())
        print("Sending successful!")
    except socket.error as e:
        print("Sending failed:", e)

s.close()


