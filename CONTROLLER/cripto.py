from cryptography.fernet import Fernet

key : str = 'zUN8HANMfa1njXCCfPpcvMkqfeFyrAdlgGS0ay19mS8='

fernet : Fernet = Fernet(key)

def encriptar(e : bytes | None) -> bytes:
    encript : bytes = fernet.encrypt(e)  # type: ignore
    return encript
 
def decriptar(e : bytes) -> bytes:
    decript : bytes = fernet.decrypt(e)
    return decript

encriptado : bytes = encriptar(b'129.148.45.165')
print(encriptado)