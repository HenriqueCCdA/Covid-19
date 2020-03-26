import matplotlib.pyplot as plt
from Pais import Pais


def main():

    paises = ['brasil.csv', 'italia.csv','USA.csv', 'Espanha.csv']

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    mk = ['o','v','^','x']

    for i, pais in enumerate(paises):
        with open('data/'+pais) as file:

            nome_pais = pais.split('.')[0]
            if nome_pais.lower() in 'usa':
                nome_pais = nome_pais.upper()
            else:
                nome_pais = nome_pais.capitalize()

            p = Pais(nome_pais)

            for line in file:
                p.data, p.dia, p.casos, p.mortes = line.strip().split(",")

        ax1.plot(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
        ax2.plot(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])

    # ... grafico casos
    ax1.set_xlim(0)
    ax1.set_xlabel('Dias')
    ax1.set_ylabel('Casos')
    ax1.grid(lw=1, ls='--')
    fig1.legend(bbox_to_anchor=(0.4, 0.85))

    # ... grafico mortes
    ax2.set_xlim(0)
    ax2.set_xlabel('Dias')
    ax2.set_ylabel('Mortes')
    ax2.grid(lw=1, ls='--')
    fig2.legend(bbox_to_anchor=(0.4, 0.85))

    fig1.savefig('fig/casos.pdf')
    fig2.savefig('fig/mortes.pdf')

if __name__ == "__main__":
    main()