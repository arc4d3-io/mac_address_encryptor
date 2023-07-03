from mac_encryptor import MACAddressEncryptor

encryptor = MACAddressEncryptor()

file_path = input("Digite o caminho do arquivo:")
key_plain = input("Digite a chave da API ")
crypted_key = encryptor.encrypt(key_plain)
encryptor.save_encryption_to_file(crypted_key, file_path)

# Exibir os valores inseridos
print("Caminho do arquivo:", file_path)
print("String:", key_plain)
