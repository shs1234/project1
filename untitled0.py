# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:29:04 2020

@author: 나
"""


def delete_a_list_element(list_data, element_value):    
    if element_value in list_data:        
        list_data.remove(element_value)        
        return list_data   
    else:        
        return "False"

list_data = ['a', 1, 'gachon', '2016.0'] 
element = float(2016) 
result = delete_a_list_element(list_data, element) 
print(result)
