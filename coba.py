import os
import platform

def list_desktop():
    system = platform.system()

    if system == "Darwin":
        desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    return desktop_dir
    # print(f"Change to Desktop directory: {desktop_dir}")

def list_txt_files_on_desktop():
    desktop_dir = list_desktop()

    if desktop_dir:
        try:
            txt_files = [file for file in os.listdir(desktop_dir) if file.endswith(".txt")]
            if txt_files:
                print(f"Text files on the Desktop: {', '.join(txt_files)}")
            else:
                print("No text files found on the Desktop.")
        except FileNotFoundError:
            print(f"Desktop directory not found: {desktop_dir}")
    else:
        print("Unsupported operating system or Desktop directory not found.")


if __name__ == "__main__":
    list_txt_files_on_desktop()