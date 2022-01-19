#!/usr/bin/env python
# coding: utf-8

# In[1]:


def PageRankParameter(final):

    # We calculate the neighbors for every node in the graph
    neigh_dic = {}
    for n, nbrs in final.adj.items():
        neigh = []
        for nbr, eattr in nbrs.items():
            neigh.append(nbr)


        neigh_dic[str(n)] = neigh


    # For every node we calculate the sum of the square radius of their edges
    sum_radius = {}
    for node in final.nodes:

        sum_edges = 0
        for nei in neigh_dic[str(node)]:

            score = final[node][nei]['rad_max_sph']
            sum_edges += score**2
        sum_radius[str(node)] = sum_edges

    #  conexion is a dictionary that saves information of the weights that every edge has in 
    # relationship with the total number of edges in the node.
    # Every edge has a radius as attribute so we are using the proportion of the square of the radius divide by
    # the sum of the square radius in the node

    flow_coef = {}
    
    for node in final.nodes:

        sub = {}
        for nei in neigh_dic[str(node)]:
            radius_node = final[node][nei]['rad_max_sph']
            all_radius = sum_radius[str(nei)] 
            sub[str(nei)] = radius_node**2/all_radius
        flow_coef[str(node)] = sub
    return neigh_dic, flow_coef 


# In[ ]:




