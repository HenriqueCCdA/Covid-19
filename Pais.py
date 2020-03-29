class Pais:

    def __init__(self, nome):
        self.__nome = nome
        self.__data = []
        self.__dia = []
        self.__casos = []
        self.__mortes = []
        self.__taxa_casos = []
        self.__taxa_mortes = []

    def percentual(self):
        return self.__mortes[-1]/self.__casos[-1]*100.e0

    def cal_taxa_de_casos(self):
        self.__taxa_casos = Pais.derivada(self.__casos)

    def cal_taxa_de_mortes(self):
        self.__taxa_mortes = Pais.derivada(self.__mortes)

    @property
    def taxa_casos(self):
        return self.__taxa_casos

    @property
    def taxa_mortes(self):
        return self.__taxa_mortes

    @property
    def tdia(self):
        return self.__tdia

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

    @staticmethod
    def derivada(x):

        deri = []
        for i in range(0, len(x) - 1):
            taxa = x[i+1] - x[i] # dc/dt
            deri.append(taxa)

        return deri
