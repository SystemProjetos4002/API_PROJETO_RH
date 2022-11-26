import mysql.connector
from mysql.connector import errorcode
from mysql.connector import CMySQLConnection,MySQLConnection

def conecta(host : str,user : str,password : str,database : str) -> CMySQLConnection | MySQLConnection:
    '''Conecta no banco Mysql'''
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def sqlComands(arg : str ) -> str | None:
    if arg == 'getlogin':
         return 'SELECT id,	nome,	login,	senha,	fk_cargo,	fk_equipe,	fk_privilegios FROM t_login;'
    else:
        pass
   
   