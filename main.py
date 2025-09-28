import numpy as np

def get_file_contents(path):
    pass

def parse_experiences(path_to_experiences):
    pass

def do_learning(experiences, Q, K, discount_factor):
    pass

def computeQ(s,a,r,s2,a2, disc_f):
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
    path_to_experiences = '' # Set this to where the file a3q2_experiences.txt is on your machine
    Q = np.zeros((11,11,4))
    K = np.zeros((11,11,4))
    # experiences_file_contents = get_file_contents(path_to_experiences)

#
# experiences = parse_experiences(experiences_file_contents)
# do_learning(experiences, Q, K, discount_factor)

