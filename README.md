## MAC Address Encryptor

The `mac_address_encryptor` package is a Python library that provides functionality for encrypting and decrypting data using a device's MAC address as the encryption key.

### Installation

You can install the `mac_address_encryptor` package using pip:

```
pip install mac_address_encryptor
```

### Usage

Here's an example of how to use the `mac_address_encryptor` package:

```python
from mac_address_encryptor import MACAddressEncryptor

# Create an instance of MACAddressEncryptor
encryptor = MACAddressEncryptor()

# Text to be encrypted
plaintext = "Text to be encrypted."

# Encrypt the text
encrypted_text = encryptor.encrypt(plaintext)
print('Encrypted Text:', encrypted_text)

# Decrypt the text
decrypted_text = encryptor.decrypt(encrypted_text)
print('Decrypted Text:', decrypted_text)
```

Make sure to have the required dependencies installed before running the code.

### Project Details

- **Name**: mac_address_encryptor
- **Version**: 0.1.0-beta
- **Description**: A Python package for encrypting and decrypting data using a device MAC Address.
- **Author**: ARC4D3
- **Author Email**: code@arc4d3.com
- **URL**: [https://github.com/arc4d3-io/mac_address_encryptor](https://github.com/arc4d3-io/mac_address_encryptor)
- **License**: MIT

### Requirements

- Python 3.8 or higher
- `pycryptodome` package (version 3.18.0 or higher)
- `file_manager` package (version 0.1.0-beta or higher)

### License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

### Development Status

This project is currently in the beta development stage.

### Support

For any questions or issues, please contact the author at code@arc4d3.com.

Feel free to contribute to the project by opening issues or submitting pull requests on the GitHub repository.

For more information, please refer to the [project repository](https://github.com/arc4d3-io/mac_address_encryptor).

