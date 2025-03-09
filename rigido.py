#Importing Libraries
from spatialmath.base import rot2
from sympy import simplify, Matrix
import spatialmath.base as base
import numpy as np

#2D CASE 
#NUMERIC
R = rot2(0.2) # Radians
det = np.linalg.det(R)
print("La matriz es\n", R)
print("y su determinante es", det)
det_RxR = np.linalg.det(np.matmul(R,R))
print("El determinante de R*R es,",  det_RxR)