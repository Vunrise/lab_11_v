import socket
import random

# Параметры Диффи-Хеллмана
p = 23  # Простое число
g = 5   # Примитивный корень

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Генерация закрытого и открытого ключей
private_key = random.randint(1, p-1)
public_key = pow(g, private_key, p)

# Отправка открытого ключа серверу
client_socket.send(str(public_key).encode())

# Получение открытого ключа от сервера
server_public_key = int(client_socket.recv(1024).decode())

# Вычисление общего ключа
shared_key = pow(server_public_key, private_key, p)
print(f"Общий секретный ключ: {shared_key}")

client_socket.close()
