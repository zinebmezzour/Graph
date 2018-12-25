#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:17:36 2018

@author: zinebmezzour
"""

#%%




import requests


localhost = "http://127.0.0.1:5000"

graph = {
            "a":["b","c"],
            "b":["d"],
            "c":["d"],
            "d" :["e"],
            "e" :[],
            "f":[]
            }


def post_upload_graph(graph):
    data  = graph 
    request = requests.post(localhost+"/upload_graph", json=data)
    if request.status_code == 200:
        return request.json()
    else:
        return print(request.status_code)


def get_degrees_of_separation(start,end,graph):
    data = graph
    request = requests.post(localhost+"/degrees_of_seperation/<start>/<end>", json=data)
    if request.status_code == 200:
        return request.json()
    else:
        return print(request.status_code)
