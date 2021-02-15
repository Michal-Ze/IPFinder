import socket as s
host = ''
host = input("Write your addres Website : ")
print(f'IP of {host} is {s.gethostbyname(host)}')