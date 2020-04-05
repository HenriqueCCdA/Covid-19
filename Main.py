import matplotlib.pyplot as plt
from Pais import Pais


def main():

    paises = ['brasil.csv', 'italia.csv','USA.csv', 'Espanha.csv', 'Portugal.csv']

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()

    mk = ['o','v','^','x','s']

    tdias0 =  5
    tdias  = 45

    for i, pais in enumerate(paises):

        p = Pais.read_file(pais, pandas=True)

        p.cal_taxa_de_casos()
        p.cal_taxa_de_mortes()
        p.cal_gf_de_casos()

        ax1.semilogy(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
#       ax1.plot(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
        ax2.semilogy(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])
#       ax2.plot(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])

        ax3.semilogy(p.dia[:-1], p.taxa_casos, label=p.nome, ls='-', marker=mk[i])
        ax4.semilogy(p.dia[:-1], p.taxa_mortes, label=p.nome, ls='-', marker=mk[i])
        ax5.semilogy(p.dia[1:-1], p.gf_casos, label=p.nome, ls='-', marker=mk[i])

        print(f"{p.nome:10} = {p.percentual():6.2f} % mortes")

    # ... grafico casos
    ax1.set_xlim(tdias0, tdias)
    ax1.set_ylim(150,400000)
    ax1.set_xlabel('Dias')
    ax1.set_ylabel('Casos')
    ax1.grid(lw=1, ls='--')
    fig1.legend(bbox_to_anchor=(0.8, 0.45))
    fig1.suptitle('Total de Casos')

    # ... grafico mortes
    ax2.set_xlim(tdias0, tdias)
    ax2.set_ylim(1,20000)
    ax2.set_xlabel('Dias')
    ax2.set_ylabel('Mortes')
    ax2.grid(lw=1, ls='--')
    fig2.legend(bbox_to_anchor=(0.8, 0.45))
    fig2.suptitle('Total de Mortes')

    # ... grafico taxa de casos
    ax3.set_xlim(tdias0,tdias)
    ax3.set_ylim(100, 40000)
    ax3.set_xlabel('Dias')
    ax3.set_ylabel('Taxa de crescimento de novos casos por dia')
    ax3.grid(lw=1, ls='--')
    fig3.legend(bbox_to_anchor=(0.8, 0.45))
    fig3.suptitle('Taxa de novos casos por dia')

    # ... grafico taxa de mortes
    ax4.set_xlim(tdias0, tdias)
    ax4.set_ylim(1, 1400)
    ax4.set_xlabel('Dias')
    ax4.set_ylabel('Taxa de novas mortes por dia')
    ax4.grid(lw=1, ls='--')
    fig4.legend(bbox_to_anchor=(0.8, 0.45))
    fig4.suptitle('Taxa de novas mortes por dia')


    # ... grafico mortes
    ax5.set_xlim(tdias0, tdias)
    ax5.set_ylim(0.5, 10)
    ax5.set_xlabel('Dias')
    ax5.set_ylabel('Fator de crescimento de casos novos')
    ax5.grid(lw=1, ls='--')
    fig5.legend(bbox_to_anchor=(0.85, 0.85))
    fig5.suptitle('Fator de crescimento dos novos casos')

    fig1.savefig('fig/casos.png')
    fig2.savefig('fig/mortes.png')
#   plt.show()

if __name__ == "__main__":
    main()

