import socket

meu_servidorTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

meu_servidorTCP.bind(("127.0.0.1", 5000))

meu_servidorTCP.listen(2)
print("Esperando mensagem TCP...")

comunicador, endereco = meu_servidorTCP.accept()
print(f"Conectado com {endereco}")

mensagem = comunicador.recv(1024).decode()
print(f"TCP: {mensagem}")

comunicador.send("TCP:olá servidor".encode())

comunicador.close()
meu_servidorTCP.close()
