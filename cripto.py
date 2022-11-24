from cryptography.fernet import Fernet

key = 'zUN8HANMfa1njXCCfPpcvMkqfeFyrAdlgGS0ay19mS8='
fernet = Fernet(key)

def encriptar(e):
    encript = fernet.encrypt(e)
    return encript

def decriptar(e):
    decript = fernet.decrypt(e)
    return decript

encriptado = encriptar(b'@g0r@vai4002')
print(encriptado)