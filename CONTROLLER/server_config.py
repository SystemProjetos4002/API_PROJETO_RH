from json import load
from CONTROLLER.cripto import Cripto



class ServerConfig:
    def __init__(self) -> None:

        self.__encoding : str = 'utf-8'

        self.__CRIPTO = Cripto()

        self.__JSON : dict[str, str] = load(open('./MODEL/server-config.json', mode='r', encoding='utf-8'))

        self.host : str = self.__CRIPTO.decriptar(
            bytes(self.__JSON['host'], self.__encoding)
        ).decode(self.__encoding)

        self.user : str = self.__CRIPTO.decriptar(
            bytes(self.__JSON['user'], self.__encoding)
        ).decode(self.__encoding)

        self.password : str = self.__CRIPTO.decriptar(
            bytes(self.__JSON['password'], self.__encoding)
        ).decode(self.__encoding)

        self.database : str = self.__CRIPTO.decriptar(
            bytes(self.__JSON['database'], self.__encoding)
        ).decode(self.__encoding)

    