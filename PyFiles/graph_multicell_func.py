#!/usr/bin/env python
# coding: utf-8

# In[3]:


def GraphMultiCell(G, vector_pos, vector_ort, pos_order, connection_cell, twentysix_faces_neigh):
    
    import networkx as nx
    from copy import deepcopy
    from networkx.relabel import relabel_nodes
    import numpy as np
    # Create a dictionary which contains one graph for every cell we want to use to calculate the 
    # pagerank coefficients. 
    # These new graphs are a copy of the one that we initialized in previous step so, we 
    # change the names and the cartesian coordinates for every node

    graph_mod= {}

    # As we mentioned earlier we are goint to name the nodes wit a number.
    # The name of the last node of the first graph plus one (because we start in 0) will give as the range in every 
    # graph.

    key_plus = sorted(list(G.nodes), reverse=True)[0] + 1

    # The names used as keys in the dictionary of graph are the ortogonal base transformations we calculated before
    # They names are very useful to know the position of the graph with respect to the origin (0,0,0).

    for i in range(len(vector_pos)):
        name = str(vector_ort[i][0])+str(vector_ort[i][1])+str(vector_ort[i][2])
        graph_mod[name] = deepcopy(G)

        mapping_name = {}
        multiplier = pos_order[name]
        for node in graph_mod[name].nodes:
#             print(node, name)
            graph_mod[name].nodes[node]['coord'] += vector_pos[i] #*box
            mapping_name[node] = node + key_plus*multiplier
        relabel_nodes(graph_mod[name], mapping=mapping_name, copy=False)

    # As you can see here it is really to see where the graph is if we now their name
    #     print('Keys of the Dictionary of Graph: {}'.format(graph_mod.keys()))


    # List with the names of the graph 

    # Now we add to the graph the edges that connect with nodes outside of the cell. We do this for every graph 
    # in the dictionary

    for j in range(len(vector_pos)):
        for neighbor in twentysix_faces_neigh:
            str_neighbor = str(neighbor[0]) + str(neighbor[1]) + str(neighbor[2]) 

            neig_loc = vector_ort[j] + neighbor
            str_neig_loc = str(neig_loc[0])+str(neig_loc[1])+str(neig_loc[2])

            if str_neig_loc in list(pos_order.keys()):
                name = str(vector_ort[j][0])+str(vector_ort[j][1])+str(vector_ort[j][2])
                multiplier_origin = pos_order[name]
                multiplier_destination = pos_order[str_neig_loc]

                for edge in connection_cell[str_neighbor]:
                    edge_1 = edge[0] + multiplier_origin*key_plus
                    edge_2 = edge[1] + multiplier_destination*key_plus
                    rad_max_sph = edge[2]
                    graph_mod[name].add_edge(edge_1, edge_2)
                    graph_mod[name].edges[edge_1, edge_2]['rad_max_sph'] = rad_max_sph

            else:
            
                first = np.where(neig_loc == 2, -1, neig_loc)
                symm_vec = np.where(first == -2, 1, first)

                name = str(vector_ort[j][0])+str(vector_ort[j][1])+str(vector_ort[j][2])
                str_neig_loc_symm = str(symm_vec[0])+str(symm_vec[1])+str(symm_vec[2])

                multiplier_origin = pos_order[name]
                multiplier_destination = pos_order[str_neig_loc_symm]

                for edge in connection_cell[str_neighbor]:
                    edge_1 = edge[0] + multiplier_origin*key_plus
                    edge_2 = edge[1] + multiplier_destination*key_plus
                    rad_max_sph = edge[2]
                    graph_mod[name].add_edge(edge_1, edge_2)
                    graph_mod[name].edges[edge_1, edge_2]['rad_max_sph'] = rad_max_sph

    final = nx.Graph()

    for key in graph_mod:
        final.add_nodes_from(graph_mod[key])
        final.add_edges_from(graph_mod[key].edges)
        for node in graph_mod[key].nodes:
            for attr in graph_mod[key].nodes[node]:
                final.nodes[node][attr] = graph_mod[key].nodes[node][attr]

        for edge in graph_mod[key].edges:
            for attr in graph_mod[key].edges[edge[0], edge[1]]:
                final.edges[edge][attr] = graph_mod[key].edges[edge][attr]
                
    return final, key_plus


# In[ ]:




