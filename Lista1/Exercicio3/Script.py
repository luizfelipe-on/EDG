# Importando os pacotes necessários:
import math
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from astropy.io import fits
from astropy.table import Table

# Importando o arquivo CSV que contém os dados dos aglomerados da MW e o salvando na variável 'tab':
tab = pd.read_csv('asu.csv')

# Verificando o header completo de 'tab':
tab.head(3008)

# Obtendo os dados necessários para Table.txt, que são RA, Dec e distância somente dos aglomerados globulares:
for i in range(0,len(tab.map)):
    if tab.Type[i] == 'g':
        print(tab.MWSC[i],tab.RAJ2000[i],tab.DEJ2000[i],tab.d[i])
        
# Importando a tabela com os dados dos aglomerados globulares:
table1 = np.loadtxt('Table.txt',dtype={'names':('identification','right_ascension','declination','distance'),
                                       'formats':('i8','f8','f8','i8')}, unpack=True, delimiter=',')

identification = table1[0]
right_ascension = table1[1]
declination = table1[2]
distance = table1[3]

# Distribuição da distância dos aglomerados globulares ao centro da Via Láctea:
r = []
for i in range(0,len(identification)):
    r.append(distance[i])
        
plt.hist(r,bins=10,range=(0,50000))
plt.title('Distribuicao das Distancias dos Aglomerados Globulares',fontsize=14)
plt.xlabel('Distancia [pc]',fontsize=12)
plt.ylabel('Frequencia',fontsize=12)
plt.show()

print('O histograma revela que mais da metade dos aglomerados globulares da Via Láctea estão a menos de 10 kpc do Sol.')
print('Como o enunciado solicita que apenas os mais distantes sejam considerados na estimativa das coordenadas')
print('equatoriais do centro da MW, devido à sua distribuição esférica, faremos um corte em 10 kpc, ou seja, apenas')
print('os aglomerados além desta distância serão considerados no cálculo das coordenadas do centro da galáxia. \n')

# Convertendo as coordenadas equatoriais em cartesianas para os aglomerados globulares além de 10 kpc:
x = []
y = []
z = []

for i in range(0,len(identification)):
    RA = math.pi/180*right_ascension[i] #já convertida de graus para radianos
    Dec = math.pi/180*declination[i] #já convertida de graus para radianos
    d = distance[i]
    
    if d > 10000:
        x.append(d*np.sin(math.pi/2-Dec)*np.cos(RA))
        y.append(d*np.sin(math.pi/2-Dec)*np.sin(RA))
        z.append(d*np.cos(math.pi/2-Dec))
        
# Obtendo as coordenadas cartesianas do centro da Via Láctea:
x_avg = np.mean(x)
y_avg = np.mean(y)
z_avg = np.mean(z)

# Convertendo-as para coordenadas equatoriais:
d_avg = (x_avg**2 + y_avg**2 + z_avg**2) ** 0.5
RA_avg = 180/math.pi * np.arctan(y_avg/x_avg) #já convertida de radianos para graus
Dec_avg = 180/math.pi * (math.pi/2 - np.arctan(np.sqrt(x_avg**2 + y_avg**2)/z_avg)) #já convertida de radianos para graus

print('Aproximação das coordenadas equatoriais do centro da MW:')
print('d =', round(d_avg,2), 'pc')
print('Dec =', round(Dec_avg,2), 'deg')
print('RA =', round(RA_avg,2), 'deg')
