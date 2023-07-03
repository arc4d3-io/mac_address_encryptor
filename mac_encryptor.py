import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import subprocess
import re
from   logger import Logger
import file_manager as FileManager

class MACAddressEncryptor():
    def __init__(self):
        self.logger = Logger(__name__)
        mac_address = self._get_mac_address()
        if mac_address is None:
            self.logger.log("Endereço MAC não encontrado. A geração da chave falhou.", level='error')
            raise ValueError("Endereço MAC não encontrado.")
        self.key = self._generate_key(mac_address)

    def _get_mac_address(self):
        try:
            output = subprocess.check_output(['ifconfig']).decode('utf-8')
            mac_address = re.findall(r'ether\s([0-9a-fA-F:]{17})', output)
            if mac_address:
                self.logger.log('MAC Address: %s' % mac_address[0], 'info')
                return mac_address[0]
        except subprocess.CalledProcessError:
            self.logger.log('Falha ao executar o comando ifconfig.', 'warning')
            return None

    def _generate_key(self, mac_address):
        try:
            return hashlib.sha256(mac_address.encode()).digest()
        except Exception as e:
            self.logger.log('Falha ao gerar a chave: %s' % str(e), 'error')
            raise

    def encrypt(self, plaintext):
        try:
            cipher = AES.new(self.key, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
            self.logger.log('Encrypted Text: %s' % ciphertext, 'debug')
            return cipher.iv + ciphertext
        except Exception as e:
            self.logger.log('Falha ao criptografar: %s' % str(e), 'error')
            raise

    def decrypt(self, ciphertext):
        try:
            iv = ciphertext[:AES.block_size]
            ciphertext = ciphertext[AES.block_size:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            self.logger.log('Decrypted Text: %s' % plaintext.decode(), 'debug')
            return plaintext.decode()
        except Exception as e:
            self.logger.log('Falha ao descriptografar: %s' % str(e), 'error')
            raise

    def save_encryption_to_file(self, encrypted_text, file_path):
        file_manager = FileManager.FileManager(file_path, binary=True)
        try:
            file_manager.write(encrypted_text)
            self.logger.log('Criptografia salva no arquivo: %s' % file_path, 'info')
        except Exception as e:
            self.logger.log('Falha ao abrir arquivo para escrita: %s' % str(e), 'error')
            raise

    def load_encryption_from_file(self, file_path):
        file_manager = FileManager.FileManager(file_path, binary=True)
        try:
            encrypted_text = file_manager.read()
            self.logger.log('Criptografia carregada do arquivo: %s' % file_path, 'info')
            return encrypted_text
        except Exception as e:
            self.logger.log('Falha ao abrir arquivo para leitura: %s' % str(e), 'error')
            return None
