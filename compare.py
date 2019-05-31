import pydct as p
import numpy as np
from scipy.fftpack import dctn

def compare():
    
    for i in range(1, 11):
        mat = np.random.rand(2**i, 2**i)
        print(mat)


compare()