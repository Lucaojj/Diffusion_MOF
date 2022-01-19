#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def GraphCell(nt2_name, pos_order):
    
    import networkx as nx
    import numpy as np
    
    # Initialize a networkx's graph. 
    # We take the information about the nodes and edges from the .nt2 file and passes it out to the graph.

    # Every node in the graph will have three attributes.
    # -Cartesian coordinate
    # -Pagerank coefficient
    # -Radius of the maximus sphere that fit in that node

    # Evey edge will have one attribute:
    # -Radius of the maximus sphere that can travel through the edge

    # We are not going to save the information about edges that connect point from outside of the cell
    
    path_nt2_file = './Nt2Files_MOF/' + nt2_name
    
    G = nx.Graph()
    
    cell_names = list(pos_order.keys())
    
    connection_cell = {cell_name:[] for cell_name in cell_names}
    
    larger_dist_atom = []
    
    pagerank_init_value = 20
    with open(path_nt2_file) as f:
        line = ' '

        while line:
            line = f.readline()

            if line == 'Vertex table:\n': 

                while line:

                    line = f.readline()

                    if line == '\n':
                        break
                    else:
                        line_list = line.split()
                        key = int(line_list[0])
                        coord_x = float(line_list[1])
                        coord_y = float(line_list[2])
                        coord_z = float(line_list[3])
                        min_dist_atom = float(line_list[4])

                        G.add_node(key, coord=np.array([coord_x, coord_y, coord_z]), rad_max_sph=min_dist_atom,
                                  pagerank=pagerank_init_value)
                        larger_dist_atom.append(min_dist_atom)

            if line == 'Edge table:\n':


                while line:

                    line = f.readline()
                    if line == '':
                        break
                    line_list = line.split()
                    
                    origin = int(line_list[0])
                    destination = int(line_list[2])
                    
                    larger_radius = float(line_list[3])
                    
                    x_sim = int(line_list[4])
                    y_sim = int(line_list[5])
                    z_sim = int(line_list[6])
                    
                    identifier = str(x_sim) + str(y_sim) + str(z_sim)
                    
                    if sum([abs(x_sim), abs(y_sim), abs(z_sim)]) == 0:
                        G.add_edge(origin, destination, rad_max_sph=larger_radius)
                        

                    else:
                        connection_cell[identifier].append((origin,destination,larger_radius))

    
    larger_node = max(larger_dist_atom)
    index_larger_node = np.argmax(larger_dist_atom)
    name_larger_node = list(G.nodes)[index_larger_node]
    
    return G, connection_cell, {'LargerNode':larger_node, 'NameLargerNode':name_larger_node} 

