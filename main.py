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

         
app = Flask(__name__)

@app.route('/get/getlogin',methods=['GET']) # type: ignore

def get():
        conexao  :CMySQLConnection | MySQLConnection | None = c.conecta(host,user,password,database)

        try:
                cursor : CursorBase | CMySQLConnection  = conexao.cursor(buffered = True)  # type: ignore

                sql = "SELECT * FROM t_area;"

                cursor.execute(sql)    # type: ignore

                result = [i for i in cursor.fetchall()]  # type: ignore

                json_result = {valor[0] : valor[1] for valor in result}

                cursor.close()

                conexao.commit()

                conexao.close()

                return json_result

        except Error :

                pass 

        
if __name__ == '__main__':

        try:
                app.run( host="192.168.0.150", port=5000,debug=True)

        except ValueError as err:

                print(f"{err}")


