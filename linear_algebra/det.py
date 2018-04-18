import numpy as np

a = [[1,2], [3,4]]
print("detA is : %d " % np.linalg.det(a))

b = [[1,2,3],
     [4,0,6],
     [7,8,9]]

b1 = [[0,6],
      [8,9]]
b2 = [[4,6],
      [7,9]]
b3 = [[4,0],
      [7,8]]

b11 = np.linalg.det(b1)
b22 = np.linalg.det(b2)
b33 = np.linalg.det(b3)

detB = int(round(np.linalg.det(b)))
detB_cal = int(round(b11- 2* b22 + 3* b33))

print( detB is detB_cal)

c = [[1,2,3,4],
     [9,4,0,6],
     [7,8,9,2],
     [2,3,5,2]]

c1 =  [[4,0,6],
       [8,9,2],
       [3,5,2]]

c2 = [[9,0,6],
      [7,9,2],
      [2,5,2]]

c3 = [[9,4,6],
      [7,8,2],
      [2,3,2]]

c4 = [[9,4,0],
      [7,8,9],
      [2,3,5]]


c11 = np.linalg.det(c1)
c22 = np.linalg.det(c2)
c33 = np.linalg.det(c3)
c44 = np.linalg.det(c4)

detC = int(round(np.linalg.det(c)))
detC_cal = int(round(c11- 2* c22 + 3* c33 + 4*c44))
print( detB is detB_cal)
