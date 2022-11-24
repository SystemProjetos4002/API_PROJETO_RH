from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from waitress import serve
import conection as c
import cripto
import json

with open('config.json', 'r') as j:
     config = json.loads(j.read())

host     = cripto.decriptar(bytes(config['connection_setings']['host'], 'utf-8')).decode("utf-8")
user     = cripto.decriptar(bytes(config['connection_setings']['user'], 'utf-8')).decode("utf-8")
password = cripto.decriptar(bytes(config['connection_setings']['password'], 'utf-8')).decode("utf-8")
database = cripto.decriptar(bytes(config['connection_setings']['database'], 'utf-8')).decode("utf-8")

conexao = c.conecta(host,user,password,database)
cursor = conexao.cursor(buffered = True) 
app = Flask(__name__)

@app.route('/get/getlogin',methods=['GET'])
def get():
        conexao = c.conecta(host,user,password,database)
        cursor = conexao.cursor(buffered = True) 
        sql = "SELECT * FROM t_area;"
        cursor.execute(sql)
        result = [i for i in cursor.fetchall()]
        json_result = {valor[0] : valor[1] for valor in result}
        cursor.close()
        conexao.commit()
        conexao.close()
        print(type(json_result))
        return json_result

        
if __name__ == '__main__':
        try:
                app.run( host="10.0.0.109", port=5000,debug=True)
        except ValueError as err:
                print(f"{err}")


