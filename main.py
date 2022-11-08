# This is a sample Python script.
import numpy as np
POINT_NUM=20
DIMENSION=3

#defined paths and distances
ideal_trajectory=np.zeros((POINT_NUM,DIMENSION))
ideal_trajectory=ideal_trajectory+3
real_trajectory=np.zeros((POINT_NUM,DIMENSION))
distance=np.zeros((POINT_NUM,DIMENSION))




def  normalize_path(ideal,real):
    ideal[:, 0] = ideal[:, 0] - ideal[0, 0]
    ideal[:, 1] = ideal[:, 1] - ideal[0, 1]
    ideal[:, 2] = ideal[:, 2] - ideal[0, 2]
    real[:, 0] = real[:, 0] - real[0, 0]
    real[:, 1] = real[:, 1] - real[0, 1]
    real[:, 2] = real[:, 2] - real[0, 2]
    return ideal,real

def distance_calculate(ideal,real,dist):
    np.add(ideal,-real,dist)
    return dist

distance_calculate(ideal_trajectory,real_trajectory,distance)

print(distance)
















