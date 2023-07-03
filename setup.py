from setuptools import setup, find_packages

setup(
    name='mac_address_encryptor',
    version='0.1.0-beta',
    description='A Python package for encrypting and decrypting data using a device MAC Address.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ARC4D3',
    author_email='repo@arc4d3.com',  # replace with your own email
    url='https://github.com/arc4d3-io/mac_address_encryptor',  # replace with your project's GitHub URL or website
    install_requires=[
        'pycryptodome>=3.18.0',  # change versions as needed
        'file_manager>=0.1.0-beta',
    ],    
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',  # or whatever minimum Python version you want to support
)
