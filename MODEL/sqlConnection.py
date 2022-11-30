from mysql.connector import connect
from CONTROLLER.server_config import ServerConfig
from mysql.connector import CMySQLConnection,MySQLConnection


class SlqConection:
    def __init__(self) -> None:
        self.__config = ServerConfig()
        

    def conecta(self) -> CMySQLConnection | MySQLConnection:
        return connect(
            host=self.__config.host, 
            user=self.__config.user, 
            password=self.__config.password, 
            database=self.__config.database
        )