from CONTROLLER.local_config import LocalConfig
from VIEW.api_routes import return_app
from waitress import serve

class Main:# Criando classe Main, classe inicial.
    
    def __init__(self) -> None:#A mesma não recebe nenhum atributo em sua iniciação
        
        try:
            
            self.config = LocalConfig()#tentando pegar configurações do servidor local, onde a api será servida
           
            serve( #criando Server waitress para a API
                
                return_app(),#Criando um objeto Flask, chamado de app para o servir no waitress 
                host=self.config.iplocal(), #pegando IP do servidor
                port=self.config.port()     #pegando porta
            )

        
        except Exception as ERROR:
            print(ERROR)


if __name__ == '__main__':
    Main()
