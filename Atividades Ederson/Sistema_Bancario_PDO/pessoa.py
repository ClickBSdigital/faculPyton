class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome and isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("Nome deve ser uma string não vazia")