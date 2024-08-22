import stepic # type: ignore
from PIL import Image # type: ignore
from cryptography.fernet import Fernet # type: ignore

print("-----------------------------------------------------------")

key=input("Enter the secret key: ")
dec=Fernet(key)

file=input("Enter the image filename to be decrypted: ")

img=Image.open(file)
decoded=stepic.decode(img)
text_dec=dec.decrypt(decoded.encode())

print("The hidden message is: "+ text_dec.decode())

print("-----------------------------------------------------------")

input("Complete (Press enter -> exit)")