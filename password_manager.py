from cryptography.fernet import Fernet
import maskpass
import base64
master = input("Enter your master password: ")

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
load_key()
"""
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password_mang.txt", "a") as f:
        f.write(name +"-"+pwd+ "\n")
        print("Account added successfully")


def view():
    # add().get()
    comfirmation = input("Re-type your master password: ")
    if comfirmation == master:

        with open("password_mang.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("-")
                print("User:"+user+"| Password:"+passw)

    else:
        pass
        # encode = base64.b64encode(pwd.encode("utf-8"))
        # print(encode)


while True:
    mode = input("Do you want to add a password or view your password? Or type close to exit:  ").lower()
    if mode == "close":
        break

    if mode == "view":
        view()
        
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue