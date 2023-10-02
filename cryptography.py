#This was an assignment for one of my Cyber Security Modules.

#pip install cryptography

import os
from cryptography.fernet import Fernet

def create_file():
    # Get the message from the user
    message = input("Enter your message: ")
    
    # Get the current working directory
    cwd = os.getcwd()
    
    # Create the file path
    file_path = os.path.join(cwd, "message.txt")
    
    # Open the file for writing
    with open(file_path, "w") as f:
        # Write the message to the file
        f.write(message)
    #print the file path of the text file that was just created.
    print("File created at:", file_path)
    #Ask users if they want to encrypt message
    encrypt_choice = input("Do you want to encrypt the message? (yes/no) ")
    if encrypt_choice.lower() == "yes":
        #Generating the encryption key:
        key = Fernet.generate_key()
        #Create an instance of the Fernet class using the key
        cipher_suite = Fernet(key)
        #Encrypt the message using the Fernet instance
        cipher_text = cipher_suite.encrypt(message.encode())
        
        # Create the file path
        file_path = os.path.join(cwd, "encrypted_message.txt")
        
        # Open the file for writing
        with open(file_path, "wb") as f:
            # Write the ciphertext to the file
            f.write(cipher_text)
        
        # Create the key path
        key_path = os.path.join(cwd, "key.key")
        
        # Save the key to a file
        with open(key_path, "wb") as f:
            f.write(key)
        # Print the file path
        print("File created at:", file_path)
        print("Encryption key has been saved in a seperate key file")
    elif encrypt_choice.lower() == "no":
        print("Thank you for using the application")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
    # Ask the user if they want to decrypt the message
    decrypt_choice = input("Do you want to decrypt the message? (yes/no) ")
    if decrypt_choice.lower() == "yes":
        # Get the key path
        key_path = os.path.join(cwd, "key.key")
        
        # Read the key from the file
        with open(key_path, "rb") as f:
            key = f.read()
            
        # Create cipher suite
        cipher_suite = Fernet(key)
        
        # Decrypt the message
        decrypted_text = cipher_suite.decrypt(cipher_text)
        
        # Create the decrypted file path
        decrypted_file_path = os.path.join(cwd, "decrypted_message.txt")
        
        # Open the file for writing
        with open(decrypted_file_path, "w") as f:
            # Write the decrypted message to the file
            f.write(decrypted_text.decode())
            # Print the file path
        print("File created at:", decrypted_file_path)
        #if user doesn't want to decrypt message print
    elif decrypt_choice.lower() == "no":
        print("Thank you for using the application")
        #print message if invalid text was typed in
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    create_file()
