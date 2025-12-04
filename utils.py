import matplotlib.pyplot as plt
import numpy as np
import math

def plot_vetores(vetores, cores=None, titulo="Vetores"):
    vetores = np.array(vetores)

   # ajuste em caso de vetor unico
    if vetores.ndim == 1:
        vetores = vetores[:, np.newaxis] 

    plt.figure(figsize=(6,6))

    if cores is None:
        cores = ['r', 'b', 'g', 'm', 'c', 'y', 'k']

     # encontra o maior valor nos dados para definir o tamanho do gráfico
    max_valor = np.max(np.abs(vetores))
    
    limite = math.ceil(max_valor * 1.1) if max_valor > 0 else 1

    for i in range(vetores.shape[1]):
        vetor = vetores[:, i]
        plt.quiver(0, 0,
                   vetor[0], vetor[1],
                   angles='xy',
                   scale_units='xy',
                   scale=1,
                   color=cores[i % len(cores)])

    plt.xlim(-limite, limite)
    plt.ylim(-limite, limite)
    
    plt.xticks(np.arange(-limite, limite+1))
    plt.yticks(np.arange(-limite, limite+1))
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(titulo)
    plt.show()