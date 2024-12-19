import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Загрузка ключей
with open("private.pem", "rb") as priv_file:
    private_key = RSA.import_key(priv_file.read())
public_key = private_key.publickey()

# Настройка клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8081))

# Обмен ключами
client_socket.send(public_key.export_key())
server_public_key = RSA.import_key(client_socket.recv(1024))

# Получение зашифрованного сообщения
encrypted_message = client_socket.recv(1024)
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)
print(f"Расшифрованное сообщение от сервера: {decrypted_message.decode()}")

client_socket.close()
