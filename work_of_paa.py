import numpy as np
import pandas as pd

weight_of_item = [1,2,5,6,7,9,11]
value_of_item = [1,6,18,22,28,40,60] 
lines_of_matrix = len(weight_of_item)
capacity_of_bag = 23

matrix = np.zeros((lines_of_matrix + 1, capacity_of_bag + 1))

for row in range(matrix.shape[0]):
    for column in range(matrix.shape[1]):
        if row == 0 or column == 0:
            matrix[row][column] = 0
        else:
            if weight_of_item[row - 1] <= column:
                matrix[row][column] = value_of_item[row - 1]
                matrix[row][column] = matrix[row][column] + matrix[row - 1][column - weight_of_item[row - 1]] 
            if matrix[row - 1][column] > matrix[row][column]:
                matrix[row][column] = matrix[row - 1][column]

print(pd.DataFrame(matrix))
