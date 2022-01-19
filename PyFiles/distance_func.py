#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def distance(final, multi_box, Y, Y1):
    # Function for the calculation of distances between axes
    import numpy as np
    dim = 3
    real_box = np.array([multi_box,multi_box,multi_box])
    
    for edge in final.edges:
        p1 = Y.dot(final.nodes[edge[0]]['coord'])
        p2 = Y.dot(final.nodes[edge[1]]['coord'])
    #     print(p1, p2)
        dist_3d = np.zeros((dim))
        for j in range(dim):
            dist = abs(p2[j]-p1[j])
            if dist > real_box[j] * 0.5:
                dist = abs(real_box[j] - dist)
            dist_3d[j] = dist
        
        final[edge[0]][edge[1]]['distance'] = np.sqrt(np.sum(np.power(Y1.dot(dist_3d), 2)))
             #- (final.nodes[edge[0]]['rad_max_sph'] + final.nodes[edge[1]]['rad_max_sph'])
    return final

