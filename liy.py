import matplotlib.pyplot as plt
import numpy as np

plt.ion()

line1, = plt.plot([1, 2, 3, 4, 5])
line2, = plt.plot([5, 4, 3, 2, 1])
path1 = plt.scatter([3, 1, 3], [1, 3, 5])
contour = plt.contour(np.arange(5*5).reshape(5, 5))

plt.waitforbuttonpress()
line1.remove()

plt.waitforbuttonpress()
line2.remove()

plt.waitforbuttonpress()
path1.remove()

plt.waitforbuttonpress()
for collection in contour.collections:
    collection.remove()

plt.waitforbuttonpress()
plt.ioff()
plt.close()