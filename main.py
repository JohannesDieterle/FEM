# 1D Finite-Elemente-Methode für den Wärmeverlauf in einem Baustoff
import matplotlib.pyplot as plt

n = 0  # Anzahl an Elemente
theta_i = 20  # Innentemperatur, °C
theta_e = -5  # Außentemperatur, °C

class Baustoff:
    def __init__(self):
        self.d = 0  # Dicke, m
        self.lambdaX = 0  # Wärmeleitfähigkeit, W/(m*K)

B_Holz = Baustoff()
B_Holz.d = 0.1
B_Holz.lambdaX = 0.1

B_Beton = Baustoff()
B_Beton.d = 0.3
B_Beton.lambdaX = 2.1

B_Dämmung = Baustoff()
B_Dämmung.d = 0.1
B_Dämmung.lambdaX = 0.035

B_Putz = Baustoff()
B_Putz.d = 0.01
B_Putz.lambdaX = 0.7

# Aufbau des Bauteils
Bauteil = [B_Putz, B_Holz, B_Beton, B_Dämmung, B_Putz]

# Gesamtdicke
ges_d = 0
for item in Bauteil:
    ges_d = ges_d + item.d

# Anzahl der Punkte
dicke_Elemente = 0.01
n = int(ges_d/dicke_Elemente)+1

# allen Punkten eine Temperatur zuweisen und Randbedingungen übernehmen
matrix_Punkte = []
for i in range(n):
    if i == 0:
        matrix_Punkte.append(theta_i)
    elif i == n-1:
        matrix_Punkte.append(theta_e)
    else:
        matrix_Punkte.append(0)

# allen Elementen die passende Wärmeleitung der Bauteile zuweisen
matrix_Elemente = []
Bauteil_zeiger = 0
i2 = 0
for i in range(n-1):
    if Bauteil[Bauteil_zeiger].d == i2*dicke_Elemente:
        i2 = 0
        Bauteil_zeiger += 1
    if len(Bauteil) == Bauteil_zeiger:
        break
    matrix_Elemente.append(Bauteil[Bauteil_zeiger].lambdaX)
    i2 += 1

def Temperaturanpassung(Punkt, matrix_Punkte, matrix_Elemente):
    # Formel um die Temperatur eines Punktes mit den Nebenpunkten anzupassen
    R_0 = matrix_Elemente[Punkt-1]/dicke_Elemente
    R_1 = matrix_Elemente[Punkt]/dicke_Elemente
    return (R_0 * matrix_Punkte[Punkt-1] + R_1 * matrix_Punkte[Punkt+1])/(R_0 + R_1)

def Iteration(Anzahl, matrix_Punkte, matrix_Elemente):
    # plt.ion()
    for i in range(Anzahl):
        for j in range(len(matrix_Punkte)):
            if j == 0 or j == len(matrix_Punkte)-1:
                continue
            matrix_Punkte[j] = Temperaturanpassung(j, matrix_Punkte, matrix_Elemente)
        # plt.plot(matrix_Punkte)
        # plt.draw()
        # plt.pause(0.0001)
        # plt.clf()
    return matrix_Punkte

Iteration(10000, matrix_Punkte, matrix_Elemente)
plt.plot(matrix_Punkte)
plt.show()
