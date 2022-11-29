from json import dumps
import MODEL.conection as c
import VIEW.Flask as Flask

from CONTROLLER.config import Config

if __name__ == '__main__':

        try:
                configsql = c.configSql()

                config = Config()

                host : str = config.iplocal()

                port : int = config.port()

                debug : bool = config.debug()

                app = Flask.tryLoginFlask(configsql["host"],configsql["user"],configsql["password"],configsql["database"])  # type: ignore
                
                app.run( host=host, port=port,debug=debug)

        except ValueError as err:

                print(f"{err}")

