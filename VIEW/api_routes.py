from mysql.connector import CMySQLConnection,MySQLConnection
from MODEL.sqlConnection import SlqConection
from MODEL.sqlCommands import SqlCommands
from CONTROLLER.cripto import Cripto
from flask import Flask, request


__app = Flask(__name__)

def return_app() -> Flask:
   
    global __sqlconn
    global __cripto
    global __sqlcommands

    __sqlconn = SlqConection()
    __sqlcommands = SqlCommands()
    __cripto = Cripto()

    return __app
    

@__app.route('/get/getlogin', methods=['GET'])
def login() -> str:
    

    conection : CMySQLConnection | MySQLConnection = __sqlconn.conecta()

    cursor = conection.cursor(buffered=True)

    command = __sqlcommands.getLogin(str(request.args.get('login')))

    cursor.execute(command)

    result : list[tuple] = [row for row in cursor.fetchall()]  # type: ignore 

    columns : list = [column[0] for column in cursor.description] # type: ignore 

    json_result : dict = {}

    if result:

        for index in range(len(result[0])):
            json_result[columns[1]] = list(result[0])[index]

        __senha : str = json_result['senha']

        conection.commit()

        cursor.close()

        conection.close()

        if request.args.get('senha') == __cripto.decriptar(__senha).decode('utf-8'):  # type: ignore

            return 'Aceito'

        else:
            return 'Senha incorreta'
        
    else:
        return 'Login incorreto'
                