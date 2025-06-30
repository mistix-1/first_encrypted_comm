# first_encrypted_comm
my first project (educational)  to create an encrypted communications bewtween 2 devices on the same network
# do not use for any production 

🔐 Secure Chat with RSA + AES Hybrid Encryption
==============================================

This project implements a secure end-to-end chat system using a hybrid encryption model:
- RSA for exchanging a symmetric key.
- AES-GCM for encrypting messages with high performance and integrity.

The communication flow is between Alice and Bob, with a Flask-based server facilitating message and key exchange.

Project Structure
-----------------
project-root/
├── alice-client.py        # Alice's client logic
├── bob-client.py          # Bob's client logic
├── chat-server.py         # Flask server acting as a relay
└── encryption_code.py     # (Not included) Contains RSA and AES cryptographic functions

> Ensure `encryption_code.py` exists in the same directory. It must include:
> - RSA key generation and encryption/decryption
> - AES-GCM encryption/decryption
> - HKDF key derivation

Cryptographic Approach
----------------------
1. Bob generates RSA keys and shares his public key via the server.
2. Alice retrieves Bob’s public key, generates a master secret, encrypts it with RSA, and sends it to the server.
3. Bob decrypts the master secret and both derive a shared AES key using HKDF.
4. All messages are encrypted with AES-GCM, base64-encoded, and relayed via the server.

How to Run
----------
1. Start the Flask Server
   python chat-server.py

2. Run Bob’s Client
   python bob-client.py

3. Run Alice’s Client (after Bob has started)
   python alice-client.py

They can now chat securely through the encrypted channel!

Features
--------
- Hybrid RSA + AES encryption
- Key exchange over insecure channel
- Integrity protection with AES-GCM
- Multi-threaded polling for message retrieval
- Base64 encoding for JSON transport compatibility

Security Notes
--------------
- This is a development implementation: the server runs over HTTP and stores data in memory.
- For production use:
  - Use HTTPS with proper SSL certificates.
  - Replace in-memory storage with a secure database.
  - Use authentication and rate-limiting.

Requirements
------------
- Python 3.7+
- Flask
- cryptography
- requests

Install dependencies:
pip install flask cryptography requests

Future Improvements
-------------------
- User authentication
- Secure key storage
- Asynchronous message delivery
- Group messaging
- WebSocket support
