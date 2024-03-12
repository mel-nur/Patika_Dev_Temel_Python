# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:08:38 2024

@author: LENOVO
"""

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def reverse_nested_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(reverse_nested_list(item)[::-1])
        else:
            result.append(item)
    return result[::-1]

# Örnek kullanım
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten_list(input_list)
output_list2 = reverse_nested_list(input_list)
print(output_list)
print(output_list2)

