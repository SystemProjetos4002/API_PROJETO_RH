from mysql.connector import CMySQLConnection,MySQLConnection
from mysql.connector.cursor import CursorBase
from flask_restful import Resource, Api
import CONTROLLER.cripto as cripto
from mysql.connector import Error
from flask import Flask, request
import MODEL.conection as c
from waitress import serve
from json import dumps
import json

def tryLoginFlask(host,user,password,database):

    app : Flask = Flask(__name__)

    @app.route('/get/getlogin',methods=['GET']) # type: ignore
    def tryLogin() -> str | None:
    
            try:
                    login = request.args.get('login')  # type: ignore

                    senha =  request.args.get('senha')
                    
                    conexao  :CMySQLConnection | MySQLConnection | None = c.conecta(host,user,password,database)

                    cursor : CursorBase | CMySQLConnection  = conexao.cursor(buffered = True)  # type: ignore
                    
                    #senha = cripto.encriptar(bytes(senha.encode('utf-8')))  # type: ignore

                    sql = c.sqlComands('getlogin',login)  # type: ignore

                    cursor.execute(sql) # type: ignore

                    result : list = [i for i in cursor.fetchall()]  # type: ignore 
                
                    columns : list = [i[0] for i in cursor.description]  # type: ignore
                
                    json_result : dict = {}

                    if result:

                            for i in range(0,len(result[0])):

                                

                                    json_result[columns[i]] = list(result[0])[i]
                            
                            senhabanco = json_result['senha']
                            
                            conexao.commit()  # type: ignore

                            cursor.close()

                            conexao.close()
   
                            if senha == cripto.decriptar(senhabanco).decode('utf8'):  # type: ignore
                                    return 'ACEITO'

                            else:
                                    return 'SENHA INCORRETA'
                    else: 
                            return 'LOGIN INEXISTENTE'

            except Error :
                    
                    pass

    @app.route('/get/getlogin',methods=['GET']) # type: ignore
    def getpedidoson() -> str | None:
        pass

    return app            

    