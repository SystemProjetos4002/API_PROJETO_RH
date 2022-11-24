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

sql = "SELECT * FROM t_area;"

cursor.execute(sql)

final_result = [i for i in cursor.fetchall()]

print(final_result)
  
cursor.close()
conexao.commit()
conexao.close()