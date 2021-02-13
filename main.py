# 2D Finite-Elemente-Methode für den Wärmeverlauf in einem Bauteil
import matplotlib.pyplot as plt
import FEM

n = 0  # Anzahl an Elemente
theta_i = 20  # Innentemperatur, °C
theta_e = -5  # Außentemperatur, °C

B_Holz = FEM.Baustoff()
B_Holz.d = 0.1
B_Holz.lambdaX = 0.1

B_Beton = FEM.Baustoff()
B_Beton.d = 0.3
B_Beton.lambdaX = 2.1

B_Dämmung = FEM.Baustoff()
B_Dämmung.d = 0.1
B_Dämmung.lambdaX = 0.035

B_Putz = FEM.Baustoff()
B_Putz.d = 0.01
B_Putz.lambdaX = 0.7

# Aufbau des Bauteils
Bauteil = [B_Putz, B_Holz, B_Beton, B_Dämmung, B_Putz]

# Gesamtdicke
ges_d = 0
for item in Bauteil:
    ges_d = ges_d + item.d

# Anzahl der Elemente pro FEM.Baustoffe
n_i = 4
n = len(Bauteil)*n_i+1

# allen Punkten eine Temperatur zuweisen und Randbedingungen übernehmen
matrix_Punkte = []
for i in range(n):
    if i == 0:
        matrix_Punkte.append(theta_i)
    elif i == n-1:
        matrix_Punkte.append(theta_e)
    else:
        matrix_Punkte.append(0)

# allen Elementen die passende Dickenaufteilung und Wärmeleitung der Baustoffe zuweisen
matrix_Elemente = []
Bauteil_zeiger = 0
i2 = 0
for i in range(n-1):
    if Bauteil[Bauteil_zeiger].d == i2*Bauteil[Bauteil_zeiger].d/n_i:
        i2 = 0
        Bauteil_zeiger += 1
    if len(Bauteil) == Bauteil_zeiger:
        break
    matrix_Elemente.append([Bauteil[Bauteil_zeiger].d/n_i, Bauteil[Bauteil_zeiger].lambdaX])
    i2 += 1

# Plot in der X-Richtung richtig strecken
x_value=[0.0]
tmp2 = 0
for i in range(len(matrix_Elemente)):
    tmp2 += round(matrix_Elemente[i][0], 4)
    x_value.append(round(tmp2, 4))

FEM.Iteration(10000, matrix_Punkte, matrix_Elemente)

# Temperaturverlauf plotten
plt.plot(x_value, matrix_Punkte)
plt.show()
