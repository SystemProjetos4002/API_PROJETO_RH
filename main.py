from mysql.connector import CMySQLConnection,MySQLConnection
from mysql.connector.cursor import CursorBase
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from mysql.connector import Error
from waitress import serve
from json import dumps
import conection as c
import cripto
import json

with open('config.json', 'r') as conf_json:
        
     config : dict[str,dict[str,str]] = json.loads(conf_json.read())

host            :str= cripto.decriptar(bytes(config['connection_setings']['host'], 'utf-8')).decode("utf-8")

user            :str= cripto.decriptar(bytes(config['connection_setings']['user'], 'utf-8')).decode("utf-8")

password        :str= cripto.decriptar(bytes(config['connection_setings']['password'], 'utf-8')).decode("utf-8")

database        :str= cripto.decriptar(bytes(config['connection_setings']['database'], 'utf-8')).decode("utf-8")

         
app : Flask = Flask(__name__)

@app.route('/get/getlogin',methods=['GET']) # type: ignore
def get():

        try:
                
                login = request.args.get('login')  # type: ignore

                senha =  request.args.get('senha')

                print(login)
                
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

                                print(f'INSERI MAIS UM {i}')

                                json_result[columns[i]] = list(result[0])[i]
                        
                        senhabanco = json_result['senha']
                        
                        conexao.commit()  # type: ignore

                        cursor.close()

                        conexao.close()

                        print(senha)

                        if senha == cripto.decriptar(senhabanco).decode('utf8'):  # type: ignore
                                return 'ACEITO'
                        else:
                                return 'SENHA INCORRETA'
                else: 
                        return 'LOGIN INEXISTENTE'

        except Error :
                
                pass 

if __name__ == '__main__':

        try:
                app.run( host="192.168.0.150", port=5000,debug=True)

        except ValueError as err:

                print(f"{err}")

