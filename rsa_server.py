import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Загрузка ключей
with open("private.pem", "rb") as priv_file:
    private_key = RSA.import_key(priv_file.read())

# Настройка сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8081))
server_socket.listen(1)
print("Сервер запущен, ожидаем подключение клиента...")

conn, addr = server_socket.accept()
print(f"Клиент подключился: {addr}")

# Получение публичного ключа клиента
client_public_key = RSA.import_key(conn.recv(1024))
conn.send(private_key.publickey().export_key())

# Шифрование и отправка сообщения
message = "Секретное сообщение от сервера".encode()
cipher = PKCS1_OAEP.new(RSA.import_key(client_public_key))
encrypted_message = cipher.encrypt(message)
conn.send(encrypted_message)

conn.close()
server_socket.close()
