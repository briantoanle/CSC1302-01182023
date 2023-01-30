# numpy

import numpy as np

'''
create a 3d array with all 0's

create an array within the range of 20 and step size 3

create a random array within range of 20 and shape of 3*3

'''
def q1():
    return np.zeros((3,3,3))
def q2():
    return np.arange(0,20,3)
def q3():
    return np.random.randint(20, size=(3, 3))

print(q1())
print(q2())
print(q3())