# Importando os pacotes necessários:
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import math

# Importando o arquivo CSV que contém as velocidades radiais e o salvando na variável 'tab': 
tab = pd.read_csv('R1.csv')
tab.head(224)

# Criando listas com as coordenadas equatoriais e as velocidades radiais:
RA = []
Dec = []
v_rad = [] 
for i in range(0,len(tab.Plx)):
    RA.append(tab.RAdeg[i])
    Dec.append(tab.DEJ2000[i])
    v_rad.append(tab.RV[i]) 
    
# Plotando o histograma de distribuição das velocidades radiais:
histogram = plt.hist(v_rad, bins=30, range=(-60,60), color='b')
plt.title('Distribuicao das Velocidades Radiais - Regiao 1', fontsize=14)
plt.xlabel('Velocidade Radial [km/s]', fontsize=12)
plt.ylabel('Frequencia', fontsize=12)
plt.show()

print('Velocidade radial média é de:', round(np.mean(v_rad),2), 'km/s')
print('Desvio padrão da amostra é de:', round(np.std(v_rad),2), 'km/s')
