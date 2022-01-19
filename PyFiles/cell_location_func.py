#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def CellLocation(nt2_name):
    
    from pymatgen.core.structure import Structure
    from math import pi, cos, sin
    import numpy as np
    
    six_letter_code = nt2_name.split('.')[0]
    
    path_nt2_file = './Nt2Files_MOF/' + nt2_name
    path_cif_file = './MOF/' + six_letter_code + '.cif'
    
    cif_structure = Structure.from_file(path_cif_file)
    
    latt = cif_structure.lattice
    
    # Angles of the cell's axis
    alpha = latt.alpha
    beta = latt.beta
    gamma = latt.gamma

    # Constant to change from degrees to radians
    cte = pi/180

    # Vectors proyections of the cell's vector over the ortogonal axis
    x_axis = latt.a
    y_axis = latt.b
    z_axis = latt.c

    # Cell's vectors
    a, b, c = round(x_axis*sin(beta*cte), 3) , 0 ,round(x_axis*cos(beta*cte), 3)
    d, e, g = round(y_axis*cos(gamma*cte), 3) ,round(y_axis*sin(gamma*cte), 3), 0
    l, m, n = 0, round(z_axis*cos(alpha*cte), 3), round(z_axis*sin(alpha*cte), 3)
    
    vector_values_latt = (a, b, c, d, e, g, l, m, n)

    # Constant that limits the maximum number of cells that could expand over every direction 
    # (axis and diagonal direction)
    r = 1

    cubic_comb = []
    
    # Each of the cell's vectors represent the length of the cell in that direction.
    # Independently of which length it is if you multiply the length of one of the vector by two it is clear
    # that the result vector will give the information about the location of the second cell in the direction
    # of the vector we multiply by two.

    # We generate the location of the cells for a cube of length equals to len(range(-r, r + 1))
    # r = 1, len(range(-r, r + 1)) = 27
    # The information of location of the cells are saved in real coordinates using the combination of the 
    # cell's vectors and in an orthogonal base transformation using as vectors the numbers (i,j,k) we use to multiply 
    # the cell's vectors
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            for k in range(-r, r+1):
                cubic_comb.append((np.array([a,b,c])*i + np.array([d,e,g])*j + np.array([l,m,n])*k,
                                   np.array([i,j,k])))

    vector_pos = []
    vector_ort = []
    # Unpack values
    # We also choose as a center the vector 0 
    
    #     print('This is the Lattice vector: {}'.format(lattice_vector.abc))

    for vec, ort in cubic_comb:
        vector_pos.append(list(vec))
        vector_ort.append(list(ort))

    # Later in this Notebook we are going to create a graph for every vector we generated in the previous step.
    # These graphs will be composed by nodes whose names will be an ordered number.
    # The names will be assigned by the order the graphs were generated.
    # That means every graph will have as the name of their nodes a range of numbers whose length will be equal 
    # to the name of the last node we create in the first graph.
    # In order to keep track of the order we create we are going to establish that order by numbered the orthogonal
    # vectors

    pos_order = {}
    i = 0
    for vector in vector_ort:
        name = str(vector[0]) + str(vector[1]) + str(vector[2]) 
        pos_order[name] = i
        i += 1

    twentysix_faces_neigh = [np.array(vector_name) for vector_name in vector_ort]
    
    return vector_pos, vector_ort, pos_order, twentysix_faces_neigh, vector_values_latt

