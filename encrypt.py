from cryptography.fernet import Fernet

# Step 1: Generate a key and save it securely
key = Fernet.generate_key()
with open('encryption.key', 'wb') as key_file:
    key_file.write(key)

# Step 2: Load the key
with open('encryption.key', 'rb') as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Step 3: Read the original CSV file
with open('books_data.csv', 'rb') as file:
    original_data = file.read()

# Step 4: Encrypt the data
encrypted_data = fernet.encrypt(original_data)

# Step 5: Save the encrypted data to a new file
with open('books_data_encrypted.csv', 'wb') as enc_file:
    enc_file.write(encrypted_data)

print("✅ Data encrypted and saved as 'books_data_encrypted.csv'")
