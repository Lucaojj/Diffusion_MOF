#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def TransfMatrix(vector_values_latt):
    import numpy as np
    a,b,c,d,e,g,l,m,n = vector_values_latt
    # Matrix to change the orthogonal base vector to the base vector of the unit cell

    A = np.array([[a,b,c],[d,e,g], [l,m,n]]).transpose()
    B1 = np.array([1, 0, 0])
    B2 = np.array([0, 1, 0])
    B3 = np.array([0, 0, 1])
    X = np.array([np.linalg.inv(A).dot(B1),np.linalg.inv(A).dot(B2),np.linalg.inv(A).dot(B3)])
    Y = X.transpose()

    # Matrix to change the base vector of the unit cell for the orthogonal base vector
    A1 = np.array([[1,0,0], [0,1,0], [0,0,1]]).transpose()
    B4 = np.array([a,b,c])#*3
    B5 = np.array([d,e,g])#*3
    B6 = np.array([l,m,n])#*3
    X1 = np.array([np.linalg.inv(A1).dot(B4),np.linalg.inv(A1).dot(B5),np.linalg.inv(A1).dot(B6)])
    Y1 = X1.transpose()

    return Y, Y1

