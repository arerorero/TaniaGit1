import numpy as np

matrix2x3 = [3, 1, 3],[6, 5, 5]
matrix3x2 = [[100, 50],[50, 100],[50, 50]]

mult = np.dot(matrix2x3,matrix3x2)
maio = mult[0][0]+mult[1][0]
junho = mult[1][1]+mult[0][1]
print("matriz final: ")
print(mult)
print("total de botões junho: ",junho)
print("total de botões maio: ",maio)