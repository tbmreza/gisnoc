import numpy as np
from scipy import signal, datasets
import matplotlib.pyplot as plt

from gisnoc import *
# from gisnoc import std_consig
# from gisnoc import std_consig, ??: accept | require_contract | contracts (https://github.com/Parquery/icontract)
std_consig.record()

image = np.asarray(datasets.ascent(), np.float64)
w = signal.windows.gaussian(51, 10.0)
image_new = signal.sepfir2d(image, w, w)
plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()


d = Consig(a=1, tx=2, c=3)
d["tx"] = 209
print(d["tx"])