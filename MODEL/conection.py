from mysql.connector import CMySQLConnection,MySQLConnection
from mysql.connector import errorcode
import mysql.connector
import CONTROLLER.cripto as cripto
import json



def conecta(host : str,user : str,password : str,database : str) -> CMySQLConnection | MySQLConnection:
    '''Conecta no banco Mysql'''
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def sqlComands(arg,login: str | None ) -> str | None:
    if arg == 'getlogin':
        return f'select login,senha from t_login where login = "{login}"'

    else:
        pass

def configSql():
    with open('MODEL/config.json', 'r') as conf_json:
        config : dict[str,dict[str,str]] = json.loads(conf_json.read())

    host            :str= cripto.decriptar(bytes(config['connection_setings']['host'], 'utf-8')).decode("utf-8")

    user            :str= cripto.decriptar(bytes(config['connection_setings']['user'], 'utf-8')).decode("utf-8")

    password        :str= cripto.decriptar(bytes(config['connection_setings']['password'], 'utf-8')).decode("utf-8")

    database        :str= cripto.decriptar(bytes(config['connection_setings']['database'], 'utf-8')).decode("utf-8")
    
    config ={}
    
    config["host"]     = host           # type: ignore

    config["user"]     = user           # type: ignore

    config["password"] = password       # type: ignore

    config["database"] = database       # type: ignore

    return config
   