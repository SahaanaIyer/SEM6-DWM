import numpy as np 
def pagerank(M, num_iterations: int = 100, d: float = 0.85):  
  N = M.shape[1] 
  v = np.random.rand(N, 1) 
  v = v / np.linalg.norm(v, 1) 
  M_hat = (d * M + (1 - d) / N) 
  for i in range(num_iterations): 
    v = M_hat @ v 
  return v 
M = np.array([[0, 0, 1, 1/2], 
             [1/3, 0, 0, 0], 
             [1/3, 1/2, 0, 1/2], 
             [1/3, 1/2, 0, 0]]) 
v = pagerank(M, 13, 1) 
print(v) 

# OUTPUT :
# [[0.3869425 ]
# [0.12906956]
# [0.29036123]
# [0.19362671]]