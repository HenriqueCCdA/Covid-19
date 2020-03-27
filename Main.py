import matplotlib.pyplot as plt
from Pais import Pais


def main():

    paises = ['brasil.csv', 'italia.csv','USA.csv', 'Espanha.csv']

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    mk = ['o','v','^','x']

    for i, pais in enumerate(paises):
        with open('data/'+pais) as file:

            nome_pais = Pais.nome_reg(pais)

            p = Pais(nome_pais)

            for line in file:
                p.data, p.dia, p.casos, p.mortes = line.strip().split(",")

        ax1.plot(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
        ax2.plot(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])

        print(f"{p.nome:10} = {p.percentual():6.2f} %")

    # ... grafico casos
    ax1.set_xlim(0,30)
    ax1.set_ylim(0,90000)
    ax1.set_xlabel('Dias')
    ax1.set_ylabel('Casos')
    ax1.grid(lw=1, ls='--')
    fig1.legend(bbox_to_anchor=(0.4, 0.85))

    # ... grafico mortes
    ax2.set_xlim(0,30)
    ax2.set_ylim(0,10000)
    ax2.set_xlabel('Dias')
    ax2.set_ylabel('Mortes')
    ax2.grid(lw=1, ls='--')
    fig2.legend(bbox_to_anchor=(0.4, 0.85))

    fig1.savefig('fig/casos.png')
    fig2.savefig('fig/mortes.png')
#   plt.show()



if __name__ == "__main__":
    main()