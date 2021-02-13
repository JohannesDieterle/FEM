"""File to outsource functions and classes"""

def Temperaturanpassung(Punkt, matrix_Punkte, matrix_Elemente):
    # Formel um die Temperatur eines Punktes mit den Nebenpunkten anzupassen
    R_0 = matrix_Elemente[Punkt-1][1]/matrix_Elemente[Punkt-1][0]
    R_1 = matrix_Elemente[Punkt][1]/matrix_Elemente[Punkt][0]
    return (R_0 * matrix_Punkte[Punkt-1] + R_1 * matrix_Punkte[Punkt+1])/(R_0 + R_1)

def Iteration(Anzahl, matrix_Punkte, matrix_Elemente):
    # plt.ion()
    for i in range(Anzahl):
        matrix_Punkte_tmp = matrix_Punkte.copy()
        for j in range(len(matrix_Punkte)):
            if j == 0 or j == len(matrix_Punkte)-1:
                continue
            matrix_Punkte[j] = Temperaturanpassung(j, matrix_Punkte_tmp, matrix_Elemente)
        # plt.plot(x_value,matrix_Punkte)
        # plt.draw()
        # plt.pause(0.0001)
        # plt.clf()
    return matrix_Punkte

