"""Bauteildatenbank"""

class Baustoff:
    def __init__(self):
        self.lambdaX = 0  # Wärmeleitfähigkeit, W/(m*K)

Holz = Baustoff()
Holz.lambdaX = 0.1

Beton = Baustoff()
Beton.lambdaX = 2.1

Dämmung = Baustoff()
Dämmung.lambdaX = 0.035

Putz = Baustoff()
Putz.lambdaX = 0.7