from mysql.connector import CMySQLConnection,MySQLConnection
from mysql.connector import errorcode
import mysql.connector



def conecta(host : str,user : str,password : str,database : str) -> CMySQLConnection | MySQLConnection:
    '''Conecta no banco Mysql'''
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def sqlComands(arg,login: str | None ) -> str | None:
    if arg == 'getlogin':
        return f'select login,senha from t_login where login = "{login}"'

    else:
        pass
   
   