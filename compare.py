import time
import os
import csv

import pydct as p
import numpy as np
from scipy.fftpack import dctn

def write_data():
    data_file = "data/data.csv"
    if not os.path.exists("data/"):
        os.makedirs("data/")

    if not os.path.exists(data_file):
        with open(data_file, "a") as logfile:
            header_writer = csv.writer(logfile, delimiter=",")
            header_writer.writerow(["size", "library", "time"])

    with open(data_file, "a") as logfile:
        for row in results:
            logfile.write(", ".join(row) + "\n")


results = []
for i in range(1, 11):
    mat = np.random.rand(2**i, 2**i)
    print("## " + str(i) + "/10")

    for j in range(10):

        print("#### " + str(j+1) + "/10")
        t0 = time.process_time()
        _ = dctn(mat, type = 2, norm = 'ortho')
        t = time.process_time() - t0
        
        results.append(["{}x{}".format(2**i, 2**i), "scipy", str(t)])

        t0 = time.process_time()
        _ = p.dct2(mat)
        t = time.process_time() - t0
        
        results.append(["{}x{}".format(2**i, 2**i), "pydct", str(t)])

write_data()
