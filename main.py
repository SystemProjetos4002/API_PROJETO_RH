from CONTROLLER.local_config import LocalConfig
from VIEW.api_routes import return_app
from waitress import serve

class Main:
    def __init__(self) -> None:
        
        try:
            
            self.config = LocalConfig()

            serve(
                return_app(),
                host=self.config.iplocal(),
                port=self.config.port()
            )

        
        except Exception as ERROR:
            print(ERROR)


if __name__ == '__main__':
    Main()
