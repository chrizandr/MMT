import numpy as np
# from homography import H_c1, H_c2, H_c3
import pdb


def read_sensor_data(data_file):
    with open(data_file, "r") as f:
        data = []
        for line in f:
            d = line.strip().split(',')
            assert len(d) >= 4
            key = d[0]
            ID = d[1]
            x, y = float(d[2]), float(d[3])


if __name__ == "__main__":
    s = "/home/chris/match_1/fh/fh.csv"
    read_sensor_data(s)
