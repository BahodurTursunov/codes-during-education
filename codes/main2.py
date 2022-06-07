import matplotlib.pyplot as plt
import math

nm = 1
a60 = math.radians(60)
h = 9


def koch(ax, ay, bx, by, n):
    ang = math.atan2(by - ay, bx - ax)
    cx = ax + (bx - ax) / 3
    dx = ax + (bx - ax) / 3 * 2
    cy = ay + (by - ay) / 3
    dy = ay + (by - ay) / 3 * 2
    h = (math.sqrt(math.pow((cx - ax), 2) + math.pow((cy - ay), 2)))

    ex = cx + h * math.cos(ang + a60)
    ey = cy + h * math.sin(ang + a60)

    n = n + 1
    if (n == nm):
        plt.plot([cx, ex], [cy, ey])
        plt.plot([ex, dx], [ey, dy])
        plt.plot([ax, cx], [ay, cy])
        plt.plot([dx, bx], [dy, by])
        return
    koch(ax, ay, cx, cy, n)
    koch(dx, dy, bx, by, n)
    koch(cx, cy, ex, ey, n)
    koch(ex, ey, dx, dy, n)


px = h * math.cos(a60)
py = h * math.sin(a60)

koch(0, 0, px, py, 0)
koch(px, py, h, 0, 0)
koch(h, 0, 0, 0, 0)
plt.axis("square")
plt.show()
