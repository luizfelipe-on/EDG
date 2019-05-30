# Importando os pacotes necessários:
from astropy.io import fits
import numpy as np
import matplotlib.pylab as plt
from astropy.table import Table
import math

# Importando a tabela com dados das estrelas de tipo F, classe V e 3 < mag aparente < 10 do catálogo de Gliese et al. (2011):
table1 = np.loadtxt('Table.txt',dtype={'names':('spectral_type','magnitude_apparent','farbe','parallax'),
                                       'formats':('S10','f8','f8','f8')}, unpack=True, delimiter=';')

spectral_type = table1[0]
magnitude_apparent = table1[1]
farbe = table1[2]
parallax = table1[3]

# Calculando distância e magnitude absoluta destas estrelas:
mag_abs = []
for i in range(0,len(farbe)):
    mag_ap = magnitude_apparent[i]
    plx = parallax[i]
    distance = float(1000)/plx
    mag_abs.append(mag_ap-5*math.log10(distance)+5)

# Obtendo a distribuição das magnitudes absolutas:
plt.hist(mag_abs, bins=17, range=(2.0,5.4))
plt.xlabel('Magnitude Absoluta',fontsize=12)
plt.ylabel('Frequencia',fontsize=12)
plt.title('Distribuicao da Magnitude Absoluta',fontsize=14)
plt.show()

# Calculando média e desvio padrão das magnitudes absolutas desta população estelar:
average = np.mean(mag_abs)
sd = np.std(mag_abs)
print('A magnitude absoluta média da amostra observada é de aproximadamente', round(average,3))
print('O desvio padrão da amostra observada é de aproximadamente', round(sd,3))
