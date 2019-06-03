# Convertendo as coordenadas equatoriais em cartesianas para os aglomerados globulares além de 10 kpc:
x = []
y = []
z = []

for i in range(0,len(identification)):
    RA = math.pi/180*right_ascension[i] #já convertida de graus para radianos
    Dec = math.pi/180*declination[i] #já convertida de graus para radianos
    d = distance[i]
    
    if d > 10000:
        x.append(d*math.sin(math.pi/2-Dec)*math.cos(RA))
        y.append(d*math.sin(math.pi/2-Dec)*math.sin(RA))
        z.append(d*math.cos(math.pi/2-Dec))

# Obtendo as coordenadas cartesianas do centro da Via Láctea:
x_avg = np.mean(x)
y_avg = np.mean(y)
z_avg = np.mean(z)

print('Coordenadas cartesianas do centro da MW são:')
print('x_avg =', x_avg, 'pc')
print('y_avg =', y_avg, 'pc')
print('z_acg =', z_avg, 'pc \n')

# Convertendo-as para coordenadas esféricas:
d_c = (x_avg**2 + y_avg**2 + z_avg**2) ** 0.5
phi_c = 180/math.pi * math.atan(y_avg/x_avg) #em deg 
theta_c = 180/math.pi * (math.atan(np.sqrt(x_avg**2 + y_avg**2)/z_avg)) #em deg

print('Coordenadas esféricas do centro da MW são:')
print('d =', d_avg, 'pc')
print('phi_c =', phi_c, 'deg')
print('theta_c =', theta_c, 'deg \n')

# É necessário fazer uma correção nos ângulos acima, pois phi não pode ser do 1 quadrante. Uma vez que x_avg e y_avg
# são negativos, phi é do 3 quadrante. Devemos portanto somar 180 deg a ele, enquanto no caso de theta, que deu 
# negativo, devemos somar 360 deg para depois subtrair 180 deg (ou simplesmente somar 180 deg):
phi_c = 180 + (180/math.pi * math.atan(y_avg/x_avg))  
theta_c = 180 + (180/math.pi * (math.atan(np.sqrt(x_avg**2 + y_avg**2)/z_avg)))

print('Coordenadas esféricas do centro da MW são:')
print('d_c =', d_avg, 'pc')
print('phi_c =', phi_c, 'deg')
print('theta_c =', theta_c, 'deg \n')

# Convertendo as coordenadas esféricas em equatoriais, sabendo que RA = phi e Dec = 90 - theta:
RA_c = phi_c
Dec_c = 90 - theta_c

print('Coordenadas equatoriais do centro da MW:')
print('d_c =', round(d_c,2), 'pc')
print('RA_c =', round(RA_c,2), 'deg')
print('Dec_c =', round(Dec_c,2), 'deg')
