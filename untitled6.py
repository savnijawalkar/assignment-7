# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:15:14 2022

@author: Dell
"""

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))