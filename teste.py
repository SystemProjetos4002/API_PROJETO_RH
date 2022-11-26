class SqlCommand:
    def __init__(self) -> None: 
        self.__connect()

    def __connect(self):
        print('conectar')
    
    def retornar(self,tabela):
        print('retornei query')