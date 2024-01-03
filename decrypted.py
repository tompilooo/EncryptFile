from cryptography.fernet import Fernet
import os
import platform

# Read the key from the file
with open("key.key", "rb") as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Function to decrypt and print the content of text files on the Desktop
def decrypt_files():
    try:
        for root, dirs, files in os.walk(os.getcwd()):
            for file_name in files:
                if file_name.endswith(".txt"):
                    file_path = os.path.join(root, file_name)

                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()

                    decrypted = fernet.decrypt(encrypted_data).decode()
                    print(f"Decrypted content of {file_name}:\n{decrypted}")
    except FileNotFoundError:
        print("Error decrypting files. Desktop directory not found.")

# Change working directory to Desktop
def change_to_desktop():
    system = platform.system()

    if system == "Windows":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    elif system == "Darwin":  # macOS
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    elif system == "Linux":
        # This assumes a standard GNOME desktop environment
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        print("Unsupported operating system.")
        return

    try:
        os.chdir(desktop_path)
        print(f"Changed working directory to Desktop: {desktop_path}")
    except FileNotFoundError:
        print(f"Desktop directory not found: {desktop_path}")

if __name__ == "__main__":
    # Change working directory to Desktop
    change_to_desktop()

    # Decrypt and print content of text files
    decrypt_files()
