class Pais:

    def __init__(self, nome):
        self.__nome = nome
        self.__data = []
        self.__dia = []
        self.__casos = []
        self.__mortes = []

    def percentual(self):
        return self.__mortes[-1]/self.__casos[-1]*100.e0

    @property
    def nome(self):
        return self.__nome

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v):
        self.__data.append(v)

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, v):
        self.__dia.append(int(v))

    @property
    def casos(self):
        return self.__casos

    @casos.setter
    def casos(self, v):
        self.__casos.append(int(v))

    @property
    def mortes(self):
        return self.__mortes

    @mortes.setter
    def mortes(self, v):
        self.__mortes.append(int(v))

    @staticmethod
    def nome_reg(pais):
        nome_pais = pais.split('.')[0]
        if nome_pais.lower() in 'usa':
            nome_pais = nome_pais.upper()
        else:
            nome_pais = nome_pais.capitalize()

        return nome_pais