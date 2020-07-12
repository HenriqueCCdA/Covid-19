import COVID19Py
import pandas as pd
from datetime import date,  datetime

def tranforma_data(date_str):
    dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    data_nova = date(dt.year, dt.month, dt.day).strftime("%d/%m/%Y")
    return data_nova

def data_por_pais(pais, ps, n_dias = 3):

    casos_confirmados = pd.DataFrame(data = pais[0]['timelines']['confirmed'])
    # removendo coluna latest
    del casos_confirmados['latest']

    # tranformado o index em coluna
    casos_confirmados['Data'] = casos_confirmados.index

    # renomeando as colunas
    casos_confirmados.columns = ['Casos', 'Data']

    # modifica o formato da data
    casos_confirmados['Data'] = casos_confirmados['Data'].apply(tranforma_data)

    # selecioando apenas com os com valores acima de 100 casos comfimados
    selecao = casos_confirmados.Casos > 200
    casos_confirmados = casos_confirmados[selecao]

    # reiniciando o index
    casos_confirmados.index = range(casos_confirmados.shape[0])

    mortes_confirmados = pd.DataFrame(data = pais[0]['timelines']['deaths'])
    # removendo coluna latest
    del mortes_confirmados['latest']

    # tranformado o index em coluna e reiniciando o index
    mortes_confirmados['Data'] = mortes_confirmados.index

    # renomeando as colunas
    mortes_confirmados.columns = ['Mortes', 'Data']

    # modifica o formato da data
    mortes_confirmados['Data'] = mortes_confirmados['Data']\
        .apply(tranforma_data)

    # selecionando apenas com os com valores acima de 100 casos comfimados
    mortes_confirmados = mortes_confirmados[selecao]

    # reiniciando o index
    mortes_confirmados.index = range(mortes_confirmados.shape[0])

    casos_e_mortes_confirmados = pd.DataFrame([casos_confirmados.Data,
                                               casos_confirmados.Casos,
                                               mortes_confirmados.Mortes]).transpose()
    casos_e_mortes_confirmados['Pais'] = ps
    casos_e_mortes_confirmados['Dias'] = casos_e_mortes_confirmados.index
    # media movel de n_dias
    casos_e_mortes_confirmados['Casos_Media'] = \
       casos_e_mortes_confirmados['Casos'].rolling(n_dias, min_periods=1).mean()
    casos_e_mortes_confirmados['Mortes_Media'] = \
        casos_e_mortes_confirmados['Mortes'].rolling(n_dias, min_periods=1).mean()

    # Caclulo de taxas
    casos_e_mortes_confirmados['Taxa_Casos_Media'] = None
    casos_e_mortes_confirmados['Taxa_Mortes_Media'] = None

    for i in range(len(casos_e_mortes_confirmados) - 1):
        dx = (casos_e_mortes_confirmados.loc[i+1,'Casos_Media'] 
              - casos_e_mortes_confirmados.loc[i, 'Casos_Media'])
        casos_e_mortes_confirmados.loc[i,'Taxa_Casos_Media'] = dx if dx > 0.0 else None

        dx = (casos_e_mortes_confirmados.loc[i+1, 'Mortes_Media'] 
            - casos_e_mortes_confirmados.loc[i, 'Mortes_Media'])
        casos_e_mortes_confirmados.loc[i,'Taxa_Mortes_Media'] = dx if dx > 0.0 else None

        dx = casos_e_mortes_confirmados.loc[i+1,'Casos'] - casos_e_mortes_confirmados.loc[i, 'Casos']
        casos_e_mortes_confirmados.loc[i,'Taxa_Casos'] = dx if dx > 0.0 else None

        dx = casos_e_mortes_confirmados.loc[i+1, 'Mortes'] - casos_e_mortes_confirmados.loc[i, 'Mortes']
        casos_e_mortes_confirmados.loc[i,'Taxa_Mortes'] = dx if dx > 0.0 else None

    return casos_e_mortes_confirmados


def read(url="https://cvtapi.nl"):

    paises = [('US', 'USA'),
              ('BR', 'Brasil'),
              ('ES', 'Espanha'),
              ('IT', 'Itália'),
              ('DE', 'Alemanha'),
              ('TR', 'Turquia'),
              ('ZA', 'África do Sul'),
              ('KR', 'Coreia do Sul'),
              ('RU', 'Russia')]

    covid19 = COVID19Py.COVID19(url=url, data_source="jhu")

    df = pd.DataFrame()
    for cd, nome in paises:
        pais = covid19.getLocationByCountryCode(cd, timelines = True)
        df_novo = data_por_pais(pais, nome, 7)
        df = pd.concat([df, df_novo], ignore_index = True)

    casos_e_mortes_confirmados = df.copy()

    casos_e_mortes_confirmados['Porcentagem'] = (casos_e_mortes_confirmados['Mortes'] /                        
                                                 casos_e_mortes_confirmados['Casos'] * 100)

    casos_e_mortes_confirmados['Porcentagem'] = (casos_e_mortes_confirmados['Porcentagem'].astype(float)).round(2)

    casos_e_mortes_confirmados['Porcentagem_Media'] = (casos_e_mortes_confirmados['Mortes_Media']
                                                         / casos_e_mortes_confirmados['Casos_Media'] * 100)

    casos_e_mortes_confirmados['Porcentagem_Media'] =\
    (casos_e_mortes_confirmados['Porcentagem'].astype(float)).round(2)

    casos_e_mortes_confirmados.to_csv('casos_e_mortes_confirmados.csv', index_label = False)