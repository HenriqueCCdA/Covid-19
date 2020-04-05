import pandas as pd

class Pais:

    def __init__(self, nome):
        self.__nome = nome
        self.__data = []
        self.__dia = []
        self.__casos = []
        self.__mortes = []
        self.__taxa_casos = []
        self.__taxa_mortes = []
        self.__gf_casos = []

    def percentual(self):
        return self.__mortes[-1]/self.__casos[-1]*100.e0

    def cal_taxa_de_casos(self):
        self.__taxa_casos = Pais.derivada(self.__casos)

    def cal_taxa_de_mortes(self):
        self.__taxa_mortes = Pais.derivada(self.__mortes)

    def cal_gf_de_casos(self):
        self.__gf_casos = Pais.taxa_crescimento(self.__casos)

    @property
    def gf_casos(self):
        return self.__gf_casos

    @property
    def taxa_casos(self):
        return self.__taxa_casos

    @property
    def taxa_mortes(self):
        return self.__taxa_mortes

    @property
    def nome(self):
        return self.__nome

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v):
        if isinstance(v, list):
            for x in v:
                self.__data.append(x)
        else:
            self.__data.append(v)

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, v):
        if isinstance(v, list):
            for x in v:
                self.__dia.append(x)
        else:
            self.__dia.append(int(v))

    @property
    def casos(self):
        return self.__casos

    @casos.setter
    def casos(self, v):
        if isinstance(v, list):
            for x in v:
                self.__casos.append(x)
        else:
            self.__casos.append(int(v))

    @property
    def mortes(self):
        return self.__mortes

    @mortes.setter
    def mortes(self, v):
        if isinstance(v, list):
            for x in v:
                self.__mortes.append(x)
        else:
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

    @staticmethod
    def taxa_crescimento(x) -> 'Taxa atual/Taxa anterior ':

        gf = []
        for i in range(1, len(x) - 1):
            taxa_f = x[i+1] - x[i]
            taxa_a = x[i] - x[i-1]
            try:
                gf.append(taxa_f/taxa_a)
            except:
                gf.append(0.0)

        return gf

    @staticmethod
    def read_file(pais, pandas = False):

        file_name = 'data/' + pais
        nome_pais = Pais.nome_reg(pais)
        p = Pais(nome_pais)
        # ... leitura com pandas do arquivo csv
        if pandas:
            data = pd.read_csv(file_name)
            data.columns = ['data', 'dia', 'casos', 'mortes']
            p.data   = list(data['data'])
            p.dia    = list(data['dia'])
            p.casos  = list(data['casos'])
            p.mortes = list(data['mortes'])
        # ..............................................................................................................

        # .... leitura manual do arquivo csv
        else:
            with open(file_name) as file:
                file.readline()
                for line in file:
                    p.data, p.dia, p.casos, p.mortes = line.strip().split(",")
        # ..............................................................................................................

        return p
