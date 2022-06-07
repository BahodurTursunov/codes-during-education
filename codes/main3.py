import matplotlib.pyplot as plt
import cmath
import numpy

nm = 10
xl = -500
xu = 1000
yl = -5000
yu = 1000

for xi in range(xl, xu, 1):
    for yi in range(yl, yu, 1):
        zn = 0
        for i in range(0, 30):
            zn = zn * zn + complex(xi / 500, yi / 500)
        if (abs(zn) < 2):
            plt.plot(xi, yi, 'bo')

plt.show()
