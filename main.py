from CONTROLLER.local_config import LocalConfig
from VIEW.api_routes import return_app

class Main:
    def __init__(self) -> None:
        
        try:
            
            self.config = LocalConfig()

            self.app = return_app()

            self.app.run(
                host=self.config.iplocal(),
                port=self.config.port(),
                debug=self.config.debug()
            )
        
        except Exception as ERROR:
            print(ERROR)


if __name__ == '__main__':
    Main()
