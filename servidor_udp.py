import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 5001))
print("Servidor UDP esperando por mensagens...")

while True:
    mensagem, endereco = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")
    resposta = "PING"
    server_socket.sendto(resposta.encode(), endereco)
