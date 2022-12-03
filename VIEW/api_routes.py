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

    __sqlconn = SlqConection() #cria variável global com a instancia de um objeto de conexões com o Mysql

    __sqlcommands = SqlCommands() #cria variável global com a instancia de um objeto de comandos do Mysql

    __cripto = Cripto() #cria variável global com a instancia de um objeto de critografia

    return __app
    

@__app.route('/get/getlogin', methods=['GET']) #rota de login no banco
def login() -> str:

    conection : CMySQLConnection | MySQLConnection = __sqlconn.conecta() #Cria uma instancia do objeto de conexão com o banco

    cursor = conection.cursor(buffered=True) #Cria um cursor

    command = __sqlcommands.getLogin(str(request.args.get('login'))) #cria a variável de verificação se o login existe

    cursor.execute(command) #executa a verificação

    result : list[tuple] = [row for row in cursor.fetchall()]  # type: ignore | cria uma lista com os valores do resultado

    columns : list = [column[0] for column in cursor.description] # type: ignore  | cria uma lista com as colunas do resultado

    json_result : dict = {}

    if result: #caso exista algum resultado

        for index in range(len(result[0])):
            json_result[columns[1]] = list(result[0])[index] #cria um dicionario com a coluna x resultado

        __senha : str = json_result['senha'] #cria variável senha

        conection.commit() #commita a conexão

        cursor.close() #fecha o cursor

        conection.close() #fecha a conexão

        if request.args.get('senha') == __cripto.decriptar(__senha).decode('utf-8'):  # type: ignore #compara a senha passada e a senha do banco

            return 'Aceito' #Caso senham iguais

        else:
            return 'Senha incorreta' #Caso sejam diferentes
        
    else:
        return 'Login incorreto' #Caso o login não exista no banco
                

@__app.route('/get/geton', methods=['GET'])  # type: ignore #rota pra pegar quem ta online
def getOrder() -> dict | None:

    if login() == 'Aceito': #verifica login

        conection : CMySQLConnection | MySQLConnection = __sqlconn.conecta() #conexão com o banco

        cursor = conection.cursor(buffered=True) #cria cursor 

        command = __sqlcommands.getOrder() #pega comando sql associado

        cursor.callproc(command) #chama a procedure

        for results in cursor.stored_results():   # type: ignore

            columns = list(results.column_names) #pega as colunas do resultado

            result = results.fetchall() #pega os valores do resultado
        
        json_result : dict = {}

        if result: # type: ignore

            for index in range(len(result[0]) -1):

                json_result[columns[index]] = list(result[0])[index] #type: ignore #cria um dicionario com o resultado

            conection.commit() #commita conexão

            cursor.close() #fecha o cursor

            conection.close() #fecha a conexão
 
            return json_result #retorna o resultado
        
        else:
            return {} #Caso o login esteja incorreto retorna um json vazio
        
    else:
        pass