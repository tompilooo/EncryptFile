import ctypes
import os

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

if __name__ == "__main__":

    # Call the function to open the README.txt file on the desktop
    open_readme_on_desktop()
