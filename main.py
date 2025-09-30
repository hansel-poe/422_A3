import numpy as np

def get_file_contents(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

def parse_experiences(path_to_experiences):
    return path_to_experiences.split(';')

def do_learning(experiences, Q, K, discount_factor):
    n_iter = len(experiences) / 3
    for i in range(n_iter):
        offset = 3 * i
        if offset + 4 >= len(experiences):#if we dont have enough inputs
            break
        s,a,r,s2,a2 = experiences[offset], experiences[offset + 1], experiences[offset + 2], experiences[offset + 3], experiences[offset + 4]
        computeQ(s, a, r, s2, a2, Q, K, discount_factor)

def computeQ(s,a,r,s2,a2, Q, K, disc_f):
    (x,y), (x2,y2) = s, s2
    alpha = 1/(K[x,y,a])
    Q[x,y,a] = Q[x,y,a] + alpha * (r + disc_f*(Q[x2,y2,a2]) - Q[x,y,a])


# These are provided by the autograder, do not overwrite them
UP, DOWN, LEFT, RIGHT, discount_factor = 0, 1, 2, 3, 0.3643
# # These will depend on if you running locally or uploading your final answers
# Q, K, experiences_file_contents

# ===============================
# ⚠️ COMMENT THIS OUT BEFORE UPLOADING ⚠️
debug_mode = True
# ===============================

if (debug_mode):
    path_to_experiences = './a3q2_experiences.txt' # Set this to where the file a3q2_experiences.txt is on your machine
    Q = np.zeros((11,11,4))
    K = np.zeros((11,11,4))
    experiences_file_contents = get_file_contents(path_to_experiences)
    # print(type(arr[0]),arr[0],type(arr[1]),arr[1])
    experiences = parse_experiences(experiences_file_contents)
    do_learning(experiences, Q, K, discount_factor)


#
# experiences = parse_experiences(experiences_file_contents)
# do_learning(experiences, Q, K, discount_factor)

