import socket
import random

# Параметры Диффи-Хеллмана
p = 23  # Простое число
g = 5   # Примитивный корень

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Сервер запущен, ожидаем подключение клиента...")

# Генерация закрытого и открытого ключей
private_key = random.randint(1, p-1)
public_key = pow(g, private_key, p)

# Ожидание клиента
conn, addr = server_socket.accept()
print(f"Клиент подключился: {addr}")

# Обмен ключами
client_public_key = int(conn.recv(1024).decode())
conn.send(str(public_key).encode())

# Вычисление общего ключа
shared_key = pow(client_public_key, private_key, p)
print(f"Общий секретный ключ: {shared_key}")

conn.close()
server_socket.close()
