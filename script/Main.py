import matplotlib.pyplot as plt
from script.Pais import Pais
from math import pow

def pg(y0, xF, dias_dobra):
    y = [y0]
    x = [0]
    f = pow(2.0, 1.0/dias_dobra)
    for xi in range(1, xF):
        y.append(y0*pow(f, xi))
        x.append(xi)
    return x, y

def main():

    paises = ['brasil.csv', 'italia.csv','USA.csv', 'Espanha.csv', 'Alemanha.csv']

    fig1, (ax1, ax2) = plt.subplots(ncols = 2, figsize=(12, 6), tight_layout = True, sharey = False)
    fig2, (ax3, ax4) = plt.subplots(ncols = 2, figsize=(12, 6), tight_layout = True, sharey = False)

    fig3, ax5 = plt.subplots(figsize=(16,6))
    fig4, ax6 = plt.subplots(figsize=(8,6))

    mk = ['o','v','^','x','s','D']

    tdias0 =  5
    tdias  = 55

#   for i in range(2,6):
#       xd, dobra_x_dias  = pg(1, tdias, i)
#       ax1.semilogy(xd, dobra_x_dias, label='Dobra a cada '+ str(i) + ' dias', ls='--')

    for i, pais in enumerate(paises):

        p = Pais.read_file(pais, pandas=True)

        # ...
        p.cal_taxa_de_casos()
        p.cal_taxa_de_mortes()
        p.cal_gf_de_casos()
        p.cal_hist_porcentual()
        # .............................................................................................................

        # ... plot
        ax1.semilogy(p.dia, p.casos , label=p.nome, ls='-', marker=mk[i])
        ax2.semilogy(p.dia[:-1], p.taxa_casos, ls='-', marker=mk[i])

        # ...
        ax3.semilogy(p.dia, p.mortes, label=p.nome, ls='-', marker=mk[i])
        ax4.semilogy(p.dia[:-1], p.taxa_mortes, ls='-', marker=mk[i])

        ax5.plot(p.dia[1:-1], p.gf_casos, label=p.nome, ls='-', marker=mk[i])
        ax6.plot(p.dia, p.hist_porcentagem, label=p.nome, ls='-', marker=mk[i])
        # .............................................................................................................

        print(f"{p.nome:10} = {p.percentual():6.2f} % mortes")

    # ... grafico casos
    ax1.set_xlim(tdias0, tdias)
    ax1.set_ylim(300,600000)
    ax2.set_xlim(tdias0,tdias)
    ax2.set_ylim(100, 50000)
    ax1.set_xlabel('Dias')
    ax2.set_xlabel('Dias')
    ax1.set_ylabel('Valores Absolutos')
    ax1.grid(lw=1, ls='--')
    ax2.grid(lw=1, ls='--')
    fig1.legend(bbox_to_anchor = (0.5, 0.45), fontsize = 14)
    ax1.set_title('Total de Casos')
    ax2.set_title('Taxa de Novos Casos por Dia')

    # ... grafico mortes
    ax3.set_xlim(tdias0, tdias)
    ax3.set_ylim(1,25000)
    ax4.set_xlim(tdias0,tdias)
    ax4.set_ylim(1, 2500)
    ax3.set_xlabel('Dias')
    ax3.set_ylabel('Mortes')
    ax4.set_xlabel('Dias')
    ax3.grid(lw=1, ls='--')
    ax4.grid(lw=1, ls='--')
    fig2.legend(bbox_to_anchor = (0.5, 0.45), fontsize = 14)
    ax3.set_title('Total de Mortes')
    ax4.set_title('Taxa de Novas Mortes por Dia')

    # ... grafico mortes
    ax5.set_xlim(tdias0, tdias)
    ax5.set_ylim(0.0, 4)
    ax5.set_xlabel('Dias')
    ax5.set_ylabel('Fator de Crescimento de Casos Novos')
    ax5.grid(lw=1, ls='--')
    fig3.legend(bbox_to_anchor=(0.85, 0.85))
    fig3.suptitle('Fator de Crescimento dos Novos Casos')

    # ... grafico porcentagem de mortes

    ax6.set_xlim(tdias0, tdias)
    ax6.set_ylim(0.0, 15)
    ax6.set_xlabel('Dias')
    ax6.set_ylabel('%')
    ax6.grid(lw=1, ls='--')
    fig4.legend(bbox_to_anchor=(0.35, 0.85))
    fig4.suptitle('Porcentagem de Mortes')

#    fig1.savefig('fig/casos.png')
#    fig2.savefig('fig/mortes.png')
#    fig4.savefig('fig/porcentagem_de_mortos.png')
    plt.show()

if __name__ == "__main__":
    main()

