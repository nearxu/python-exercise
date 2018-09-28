import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

labels = 'a','b','c','d'
size = [15,20,30,45]

plt.pie(size,labels=labels)
plt.axis('equal')
plt.show()
