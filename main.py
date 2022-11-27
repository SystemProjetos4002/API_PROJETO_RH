from json import dumps
import MODEL.conection as c
import VIEW.Flask as Flask

if __name__ == '__main__':

        try:
                configsql = c.configSql()

                app = Flask.tryLoginFlask(configsql["host"],configsql["user"],configsql["password"],configsql["database"])  # type: ignore
                
                app.run( host="192.168.0.150", port=5000,debug=True)

        except ValueError as err:

                print(f"{err}")

