import matplotlib.pyplot as plt
from Pais import Pais


def main():

    paises = ['brasil.csv', 'italia.csv','USA.csv', 'Espanha.csv', 'Portugal.csv']

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
#   fig3, ax3 = plt.subplots()
#   fig4, ax4 = plt.subplots()

    mk = ['o','v','^','x','s']

    tdias = 16

    for i, pais in enumerate(paises):
        with open('data/'+pais) as file:

            nome_pais = Pais.nome_reg(pais)

            p = Pais(nome_pais)

            for line in file:
                p.data, p.dia, p.casos, p.mortes = line.strip().split(",")

        p.cal_taxa_de_casos()
        p.cal_taxa_de_mortes()
        ax1.plot(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
        ax2.plot(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])
#       ax1.semilogy(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
#       ax2.semilogy(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])
#       ax3.plot(p.dia[:-1], p.taxa_casos, label=p.nome, ls='-', marker=mk[i])
#       ax4.plot(p.dia[:-1], p.taxa_mortes, label=p.nome, ls='-', marker=mk[i])

        print(f"{p.nome:10} = {p.percentual():6.2f} % mortes")

    # ... grafico casos
    ax1.set_xlim(0, tdias)
    ax1.set_ylim(1, 10000)
    ax1.set_xlabel('Dias')
    ax1.set_ylabel('Casos')
    ax1.grid(lw=1, ls='--')
    fig1.legend(bbox_to_anchor=(0.4, 0.85))

    # ... grafico mortes
    ax2.set_xlim(0, tdias)
    ax2.set_ylim(0.1, 1000)
    ax2.set_xlabel('Dias')
    ax2.set_ylabel('Mortes')
    ax2.grid(lw=1, ls='--')
    fig2.legend(bbox_to_anchor=(0.4, 0.85))

    # ... grafico taxa de casos
#   ax3.set_xlim(0,tdias)
#   ax3.set_ylim(0, 30000)
#   ax3.set_xlabel('Dias')
#   ax3.set_ylabel('Taxa de crescimento de casos por dia')
#   ax3.grid(lw=1, ls='--')
#   fig3.legend(bbox_to_anchor=(0.4, 0.85))

    # ... grafico taxa de mortes
#   ax4.set_xlim(0, tdias)
#   ax4.set_ylim(0, 1000)
#   ax4.set_xlabel('Dias')
#   ax4.set_ylabel('Taxa de mortes por dia')
#   ax4.grid(lw=1, ls='--')
#   fig4.legend(bbox_to_anchor=(0.4, 0.85))

    fig1.savefig('fig/casos.png')
    fig2.savefig('fig/mortes.png')
#   plt.show()



if __name__ == "__main__":
    main()