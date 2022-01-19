#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def backpedal(start_vertex, target, searchResult):

    node = target

    backpath = [node]

    path = []

    while node != start_vertex:

        backpath.append(searchResult[node])

        node = searchResult[node]

    for i in range(len(backpath)):

        path.append(backpath[-i - 1])

    return path 

