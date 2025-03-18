from cryptography.fernet import Fernet
import os

# Function to generate and save a key if it doesn't exist
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("New encryption key generated and saved as 'secret.key'.")
    else:
        print("Encryption key already exists.")

# Function to load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    cipher_suite = Fernet(key)
    try:
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
        return decrypted_message
    except:
        return "Error: Invalid encryption key or message!"

# Main function to handle user input
def main():
    generate_key()  # Ensure key exists
    while True:
        print("\n[1] Encrypt a message")
        print("[2] Decrypt a message")
        print("[3] Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            encrypted = encrypt_message(message)
            print(f"Encrypted Message: {encrypted.decode()}")

        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            try:
                decrypted = decrypt_message(encrypted_message.encode())
                print(f"Decrypted Message: {decrypted}")
            except:
                print("Invalid input! Please enter a valid encrypted message.")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
