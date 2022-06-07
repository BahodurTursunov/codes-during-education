import numpy as np
import matplotlib.pyplot as plt

# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

# число точек по горизонтали и вертикали
ppoints, qpoints = 200, 200

# максимальное количество итераций
max_iterations = 300

# если ушли на это расстояние, считаем, что ушли на бесконечность
infinity_border = 100

# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен нулями
image = np.zeros((ppoints, qpoints))

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        c = p + 1j * q
        # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
        # идёт о комплексном числе, а не о переменной j, мы пишем 1j
        z = 0
        for k in range(max_iterations):
            z = z ** 2 + c
            # Самая Главная Формула
            if abs(z) > infinity_border:
                # если z достаточно большое, считаем, что последовательость
                # ушла на бесконечность
                # или уйдёт
                # можно доказать, что infinity_border можно взять равным 4
                image[ip, iq] = 1
                # находимся вне M: отметить точку как белую
                break
plt.xticks([])
plt.yticks([])
# выключим метки на осях
plt.imshow(-image.T, cmap='Greys')
# транспонируем картинку, чтобы оси были направлены правильно
# перед image стоит знак минус, чтобы множество Мандельброта рисовалось
# чёрным цветом
plt.show()
