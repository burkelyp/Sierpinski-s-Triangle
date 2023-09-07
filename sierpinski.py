import random
import numpy as np
import matplotlib.pyplot as plt

x = [0, 100, 200]
y = [0, 200, 0]

plt.plot(x, y, c='black')
plt.plot([0, 200], [0, 0], c='black')
plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.box(False)

xpt1 = random.randint(0, 200)
if xpt1 <= 100:
    y_constraint = 2 * xpt1
else:
    y_constraint = (-2 * xpt1) + 400
ypt1 = random.randint(0, y_constraint)

x_points = [xpt1]
y_points = [ypt1]

for i in range(100000):
    pt = random.randint(0, 2)
    xx = np.mean([x[pt], x_points[-1]])
    yy = np.mean([y[pt], y_points[-1]])
    x_points.append(xx)
    y_points.append(yy)

plt.scatter(x_points, y_points, s=.5, c='red')
plt.show()
