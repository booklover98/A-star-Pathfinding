# A* Pathfinding
Using OSMnx, NetworkX and Folium

This repository was created in conjunction with a Course Project: Introduction to AI, Assignments [UOIT, W2019]

### Authors
Samantha Husack


### Assignment Requirements 
- Write an A* Algorithm that uses OSM and HTG files to find a shortest walking path between two addresses/nodes

### Problem Statement
This assignment is developed for a cross-listed (SOFE + CSCI) Intro to Artificial Intelligence course taught as part of a semester-long study for city of Oshawa. 
This is a city in Ontario, Canada,on the Lake Ontario shoreline. 
In this assignment, we will be using the characteristics of streets and elevation changes to try to find optimal routes for walking through city of Oshawa. 
The basic underlying structure will use A* to find the "shortest" path, but it will be up to you to decide how to define shortest, and to make sure your heuristics work with the definition that you make. 
In particular, developing a cost function and appropriate (admissible) heuristic given that cost function require a bit of care.

You may develop a graphical solution to this problem, as it will probably assist in your debugging process. 
To assist you in this, some startup code is provided that reads in each of the two data sets and creates a GUI window with some lines and circles.
Your final solution should be able to take (in some form) two OSM nodes and return the shortest path between them along with the expected time to walk along the path. 
You must use the elevation change and distance between nodes as part of your calculations, but beyond that you may choose your path costs in any way you believe is reasonable. 
Note that when calculating distances, one degree of latitude is larger than one degree of longitude - the given code has some useful information in this regard.

