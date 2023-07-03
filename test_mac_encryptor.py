import unittest
import os
from mac_encryptor import MACAddressEncryptor

class TestMACAddressEncryptor(unittest.TestCase):
    def setUp(self):
        self.encryptor = MACAddressEncryptor()
        self.test_plaintext = "Hello, World!"
        self.test_file_path = "test_encrypted.bin"
        self.test_crypttext = ""

    def tearDown(self):
        # Remove o arquivo de teste após cada teste
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_encrypt_and_decrypt(self):
        # Criptografa o texto de teste
        encrypted_text = self.encryptor.encrypt(self.test_plaintext)

        self.test_crypttext = encrypted_text

        # Descriptografa o texto criptografado
        decrypted_text = self.encryptor.decrypt(encrypted_text)

        # Verifica se o texto descriptografado é igual ao texto original
        self.assertEqual(decrypted_text, self.test_plaintext)

    def test_save_and_load_encryption_to_file(self):

        encrypted_text = self.encryptor.encrypt(self.test_plaintext)

        self.test_crypttext = encrypted_text        
        # Criptografa o texto de teste e salva no arquivo
        self.encryptor.save_encryption_to_file(self.test_crypttext, self.test_file_path)

        # Carrega a criptografia do arquivo
        loaded_encryption =  self.encryptor.decrypt(self.encryptor.load_encryption_from_file(self.test_file_path))

        # Verifica se a criptografia carregada é igual ao texto original
        self.assertEqual(loaded_encryption, self.test_plaintext)

if __name__ == '__main__':
    unittest.main()
