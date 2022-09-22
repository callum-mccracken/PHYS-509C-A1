"""For goofing around"""

import numpy as np
import matplotlib.pyplot as plt

x1, x2 = np.meshgrid(*[np.arange(0.001, 0.999, 0.001)]*2)
plt.scatter(x1, x2)
plt.show()

y1 = x1 / x2
y2 = x1 * x2
plt.scatter(y1, y2, s=0.1)
plt.scatter(y1, 1/y1, s=0.1, c='k')
plt.show()

