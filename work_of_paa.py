import numpy as np
import pandas as pd

weight_of_item = [1,2,5,6,7,9,11]
value_of_item = [1,6,18,22,28,40,60] 
lines_of_matrix = len(weight_of_item)
capacity_of_bag = 23

matrix = np.zeros((lines_of_matrix + 1, capacity_of_bag + 1))
print(matrix.shape)

for row in range(matrix.shape[0]-1):
    for column in range(matrix.shape[1]):
        print(row,column)
        if row == 0 or column == 0:
            matrix[row][column] = 0
        else:
            print(value_of_item[row])
            if value_of_item[row] <= column:
                matrix[row][column] = value_of_item[row]
                matrix[row][column] = matrix[row - 1][column - row] + value_of_item[row] 
            if matrix[row][column - 1] > matrix[row][column]:
                 matrix[row][column] = matrix[row][column - 1]

print(pd.DataFrame(matrix))
