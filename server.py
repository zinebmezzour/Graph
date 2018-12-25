#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:15:22 2018

@author: zinebmezzour
"""

#%%

from flask import Flask, jsonify, request


server = Flask("Graph server")

#@server.route("/see_graph")
#def see_graph():
#    return jsonify(graph)

@server.route("/upload_graph", methods = ["POST"])    
def upload_graph():
    graph = request.get_json()
    
    return jsonify({"Message":"New graph uploaded","Graph":graph})


     
@server.route("/degrees_of_seperation/<start>/<end>", methods = ["POST"])    
def degrees_of_separation(start,end,path=[],graph=""):
   
    graph = request.get_json()
    
#    print(jsonify(graph))
#    graph = jsonify(graph)

    path = path + [start]
    
    if start == end:
        degree = len(path) - int(2)
        if degree == 0:
            return jsonify("direct connection")
        else:
            return jsonify(degree)
    
    if start not in graph:
        return jsonify("Start not in graph")
    
    for conn in graph[start]:
        if conn not in path:
            new_path = degrees_of_separation(conn,end,path)
            
            if new_path is not None:
                return new_path
            
    return jsonify(None) 


server.run()  
