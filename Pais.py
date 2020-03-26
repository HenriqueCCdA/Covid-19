class Pais:

    def __init__(self, nome):
        self.__nome = nome
        self.__data = []
        self.__dia = []
        self.__casos = []
        self.__mortes = []

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
