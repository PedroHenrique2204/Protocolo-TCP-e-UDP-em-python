import socket
A=input("TCP OU UDP: ")

if A=="TCP":
    cliente_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_TCP.connect(("127.0.0.1", 5000))
    cliente_TCP.send('TESTE_TCP'.encode())
    mensagem = cliente_TCP.recv(1024).decode()
    print(f"Mensagem recebida do servidor: {mensagem}")
    cliente_TCP.close()
if A=="UDP":
    cliente_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente_UDP.connect(("127.0.0.1", 5001))
    cliente_UDP.send('TESTE_UDP'.encode())
    mensagem = cliente_UDP.recv(1024).decode()
    print(f"Mensagem recebida do servidor: UDP {mensagem}")


