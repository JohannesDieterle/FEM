# 2D Finite-Elemente-Methode für den Wärmeverlauf in einem Bauteil
import matplotlib.pyplot as plt
import FEM
import FEM_elements

theta_i = 20  # Innentemperatur, °C
theta_e = -5  # Außentemperatur, °C
r_si = 0.13 # Übergangswiderstand

# Aufbau des Bauteils
Bauteil = [[FEM_elements.Putz, 0.01],
           [FEM_elements.Beton, 0.2],
           [FEM_elements.Dämmung, 0.18],
           [FEM_elements.Putz, 0.01]]

# Gesamtdicke
ges_d = 0
for item in Bauteil:
    ges_d = ges_d + item[1]

# Anzahl der Elemente pro Baustoff
n_i = 4
n = len(Bauteil)*n_i+3

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
    if i == 0:
        matrix_Elemente.append([0.01, r_si*100])
        continue
    elif i == n-2:
        matrix_Elemente.append([0.01, 4])
        continue
    if Bauteil[Bauteil_zeiger][1] == i2*Bauteil[Bauteil_zeiger][1]/n_i:
        i2 = 0
        Bauteil_zeiger += 1
    if len(Bauteil) == Bauteil_zeiger:
        break
    matrix_Elemente.append([Bauteil[Bauteil_zeiger][1]/n_i, Bauteil[Bauteil_zeiger][0].lambdaX])
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
