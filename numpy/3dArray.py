import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for i in arr:
  for j in i:
        for k in j:
            print(k)
print (arr.shape)