from json import load

class LocalConfig:

    def __init__(self) -> None:

        self.__json : dict = load(open('./local-config.json', mode='r', encoding='utf-8')) #Ao instanciar o objeto o mesmo abre o JSON descrito

    def iplocal(self) -> str:

        return self.__json['iplocal'] #retorna o ip local do json
    
    def port(self) -> int:

        return self.__json['port'] #retorna a porta do ip local
    
