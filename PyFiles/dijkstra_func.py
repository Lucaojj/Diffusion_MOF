#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dijkstra(start_vertex, target, parents, final, tol, neigh_dic):
    from queue import PriorityQueue
    from math import pi
    # Dictionary with keys = vertices and values = weights of the vertices (set as infinity at the start)
    D = {}
    visited = []
    node_list = list(final.nodes)

    D = {v:float('inf') for v in node_list}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        if current_vertex == target:
#             print('Target vertex: ' + str(target) + ' reached')
            break
        else:

            visited.append(current_vertex)


            # Loop for every vertex of the net
            for neighbor in neigh_dic[str(current_vertex)]:
#                         if self.edges[current_vertex][neighbor] != -1:
               
                distance_edge = final[current_vertex][neighbor]['distance']

                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance_edge
                    if (new_cost < old_cost and (final.nodes[neighbor]['rad_max_sph']>tol and final[current_vertex][neighbor]['rad_max_sph']>tol)):
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        parents[neighbor] = current_vertex
                        
                        
                        
    node = target

    backpath = [node]

    path = []

    while node != start_vertex:

        backpath.append(parents[node])

        node = parents[node]

    for i in range(len(backpath)):

        path.append(backpath[-i - 1])

        
    
    distance_path = []
    volume_path = []
    for i in range(len(path)-1):

        distance_path.append(final[path[i]][path[i+1]]['distance'])
        
        edge_dist = final[path[i]][path[i+1]]['distance'] - final.nodes[path[i]]['rad_max_sph'] - final.nodes[path[i+1]]['rad_max_sph']
        square_radius = final[path[i]][path[i+1]]['rad_max_sph']**2
        edge_vol = edge_dist*square_radius*pi
        
        pore_vol = ((final.nodes[path[i]]['rad_max_sph']**3) + (final.nodes[path[i+1]]['rad_max_sph']**3))*(4/3)*pi
        
        volume_path.append(edge_vol + pore_vol)#final[path[i]][path[i+1]]['distance'] * (final[path[i]][path[i+1]]['rad_max_sph']**2)*pi
    total_distance = sum(distance_path)   
    total_volume = sum(volume_path)
    return path, total_distance, total_volume

    


# In[ ]:




