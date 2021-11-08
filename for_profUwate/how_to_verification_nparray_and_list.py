# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:55:11 2021

@author: arailab
"""
import numpy as np
# how to verif
node_size = 10
packet_size = 10
nodes_list = [[[0]*packet_size]*node_size]
nodes_array = np.array([[[0]*node_size]*packet_size])
print("nodes_list", nodes_list)
print("nodes_array",nodes_array)
# how to refer
print(nodes_list[0][0])
print(nodes_array[0][0])
print(nodes_array[0,0])
print(nodes_array[0,0,0])