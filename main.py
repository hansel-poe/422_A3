import numpy as np
from ast import literal_eval
from enum import Enum

#Returns int representation of action
def getNum(letter):
    if letter == 'U':
        return 0
    elif letter == 'D':
        return 1
    elif letter == 'L':
        return 2
    elif letter == 'R':
        return 3

def get_file_contents(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

def parse_experiences(path_to_experiences):
    return path_to_experiences.split(';')

#Returns updated q and k
def do_learning(experiences, q, k, discount_factor):
    n_iter = len(experiences) // 3 #integer division (floors result)
    for i in range(n_iter):
        offset = 3 * i
        if offset + 4 >= len(experiences):#if we are missing one of s,a,r,s',a'
            break
        s,a,r,s2,a2 = (literal_eval(experiences[offset]), getNum(experiences[offset + 1].strip()), float(experiences[offset + 2]),
                       literal_eval(experiences[offset + 3]), getNum(experiences[offset + 4].strip()))

        # adjusts index
        s = (s[0] - 1, s[1] - 1)
        s2 = (s2[0] - 1, s2[1] - 1)
        computeQ(s, a, r, s2, a2, q, k, discount_factor)
    # flips grids vertically
    return np.flipud(q), np.flipud(k)

#Note that this function assumes (0,0) as top left
def computeQ(s,a,r,s2,a2, q, k, disc_f):
    (x,y), (x2,y2) = s, s2
    k[x, y, a] += 1
    alpha = 1/(k[x,y,a])
    q[x,y,a] = q[x,y,a] + alpha * (r + disc_f*(q[x2,y2,a2]) - q[x,y,a])

# These are provided by the autograder, do not overwrite them
# UP, DOWN, LEFT, RIGHT, discount_factor = 0, 1, 2, 3, 0.3643
# # These will depend on if you running locally or uploading your final answers
# Q, K, experiences_file_contents

# ===============================
# ⚠️ COMMENT THIS OUT BEFORE UPLOADING ⚠️
# debug_mode = True
# ===============================

if (debug_mode):
    path_to_experiences = './a3q2_experiences.txt' # Set this to where the file a3q2_experiences.txt is on your machine
    Q = np.zeros((11,11,4))
    K = np.zeros((11,11,4))
    experiences_file_contents = get_file_contents(path_to_experiences)
    experiences = parse_experiences(experiences_file_contents)

    # playing with array index (just for experimenting)
    # Q[10,2,3] = 46
    # Q[10,1,3] = 21
    # Q[0,4,3] = 20
    # Q_r = Q[:,:,3]
    # print(Q)
    # print(Q_r)
    # Q_flip = np.flip(Q, 0)
    # Q_flip_r = Q_flip[:,:,3]
    # print(Q_flip)
    # print(Q_flip_r)

    #Calling the functions
    Q, K = do_learning(experiences, Q, K, discount_factor)
    print('Q:\n', Q)
    print('K:\n', K)

experiences = parse_experiences(experiences_file_contents)
Q,K = do_learning(experiences, Q, K, discount_factor)

