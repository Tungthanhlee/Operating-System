import numpy as np

# banker algorithm
PROCESSES = np.array([0, 1, 2, 3,4]) 
AVAIL = np.array([3,2,1,1]) 
MAXM = np.array([
    [6,0,1,2],
    [1,7,5,0],
    [2,3,5,6],
    [1,6,5,3],
    [1,6,5,6],
]) 
ALLOT = np.array([
    [4,0,0,1],
    [1,1,0,0],
    [1,2,5,4],
    [0,6,3,3],
    [0,2,1,2],
])


# resource request
PROCESS_TH = 1
REQUEST = np.array([1,0,2])

# deadlock detection
DL_PROCESSES = np.array([0,1,2,3,4])
DL_AVAIL = np.array([0,0,0])
DL_ALLOT = np.array([
    [0,1,0],
    [2,0,0],
    [3,0,3],
    [2,1,1],
    [0,0,2],
])
DL_REQUEST = np.array([
    [0,0,0],
    [2,0,2],
    [0,0,0],
    [1,0,0],
    [0,0,2],
])
