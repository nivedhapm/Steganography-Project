import stepic # type: ignore
from PIL import Image # type: ignore
from cryptography.fernet import Fernet # type: ignore
print("-----------------------------------------------------------")
key=Fernet.generate_key()
print("Secret key: ",key)
enc=Fernet(key)

text=input("Enter the message to be encrypted: ")
text_enc=enc.encrypt(text.encode())

file=input("Enter the image filename: ")

img=Image.open(file)
img_stegano=stepic.encode(img, text_enc)

img_stegano.save("Encrypted_Image.png")
print("-----------------------------------------------------------")

input("Complete (Press enter -> exit)")


