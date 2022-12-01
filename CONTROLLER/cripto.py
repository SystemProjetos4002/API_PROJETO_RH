from cryptography.fernet import Fernet

class Cripto:
    def __init__(self) -> None:
        
        self.__KEY : str = 'zUN8HANMfa1njXCCfPpcvMkqfeFyrAdlgGS0ay19mS8='

        self.__fernet = Fernet(self.__KEY)

    def encriptar(self, object : bytes) -> bytes:
        return self.__fernet.encrypt(object)

    def decriptar(self, object : bytes) -> bytes:
        return self.__fernet.decrypt(object)