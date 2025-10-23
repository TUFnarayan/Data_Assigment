from cryptography.fernet import Fernet

with open('encryption.key', 'rb') as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open('books_data_encrypted.csv', 'rb') as enc_file:
    encrypted_data = enc_file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open('books_data_decrypted.csv', 'wb') as dec_file:
    dec_file.write(decrypted_data)

print("✅ Data decrypted and saved as 'books_data_decrypted.csv'")
