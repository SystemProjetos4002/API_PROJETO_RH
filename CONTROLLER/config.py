from json import load

class Config:
    def __init__(self) -> None:
        self.__json : dict = load(open('./config.json', mode='r', encoding='utf-8'))

    def iplocal(self) -> str:
        return self.__json['iplocal']
    
    def port(self) -> int:
        return self.__json['port']
    
    def debug(self) -> bool:
        return self.__json['debug']
