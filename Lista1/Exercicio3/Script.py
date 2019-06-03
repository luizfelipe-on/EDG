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
        print tab.MWSC[i],tab.RAJ2000[i],tab.DEJ2000[i],tab.d[i]

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
        
plt.hist(r,bins=10,range=(0,50000),color='b')
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
        x.append(d*math.cos(Dec)*math.cos(RA))
        y.append(d*math.cos(Dec)*math.sin(RA))
        z.append(d*math.sin(Dec))

# Obtendo as coordenadas cartesianas do centro da Via Láctea:
x_avg = np.mean(x)
y_avg = np.mean(y)
z_avg = np.mean(z)

print('Coordenadas cartesianas do centro da MW são:')
print('x_avg =', round(x_avg,2), 'pc')
print('y_avg =', round(y_avg,2), 'pc')
print('z_acg =', round(z_avg,2), 'pc \n')

# Convertendo-as para coordenadas esféricas:
d_c = np.sqrt(x_avg**2 + y_avg**2 + z_avg**2)
phi_c = 180/math.pi * math.atan(y_avg/x_avg) #em deg 
theta_c = 180/math.pi * (math.atan(np.sqrt(x_avg**2 + y_avg**2)/z_avg)) #em deg

print('Coordenadas esféricas do centro da MW são:')
print('d_c =', round(d_c,2), 'pc')
print('phi_c =', round(phi_c,2), 'deg')
print('theta_c =', round(theta_c,2), 'deg \n')

print('É necessário fazer uma correção nos ângulos acima:')
print('Como x_avg e y_avg são negativos, phi_c não pode ser do 1o quadrante, mas do 3o. Devemos então somar 180 deg a ele;')
print('Como theta_c não pode ser negativo, devemos somar 360 deg a ele para depois subtrair 180 deg (ou seja, somar 180 deg). \n')

phi_c = 180 + (180/math.pi * math.atan(y_avg/x_avg))  
theta_c = 180 + (180/math.pi * (math.atan(np.sqrt(x_avg**2 + y_avg**2)/z_avg)))

print('Coordenadas esféricas do centro da MW (CORRIGIDAS) são:')
print('d_c =', round(d_c,2), 'pc')
print('phi_c =', round(phi_c,2), 'deg')
print('theta_c =', round(theta_c,2), 'deg \n')

# Convertendo as coordenadas esféricas em equatoriais, sabendo-se que RA = phi e Dec = 90 - theta, temos:
RA_c = phi_c
Dec_c = 90 - theta_c

print('Coordenadas equatoriais do centro da MW:')
print('d_c =', round(d_c,2), 'pc')
print('RA_c =', round(RA_c,2), 'deg')
print('Dec_c =', round(Dec_c,2), 'deg')
