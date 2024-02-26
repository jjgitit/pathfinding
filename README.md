
# PathFinder Visualizer
This project aims to visually demonstrate pathfinding algorithms(default : A* Algorithm). It shows current position and paths that are currently being considered.

# Table of Content
* [Technologies-and-setup](#Technologies-and-setup)
* [Features](#Features)
* [Todo](#Todo)

# Technologies and Setup
* Python 3.11.5
* Pygame 2.5.1
PathFinding Visualizer requires Pygame. To install Pygame, you must have Python installed in your system. To check if Python is installed, 
$ python3 --version
If your terminal does not raise any error and displays the version of your Python, it means Python3 is installed on your environment.
To download Pygame,
$ pip3 install pygame
Then type,
$ import pygame
If you see the latest pygame version on your terminal, we are good to go now.

# Features
To get started, right click to set a starting point and end point. After setting these two positions, you can right-click to set barriers around the grid. Pathfiding Algorithm will find the shortest distance going around barriers if obstructed.
* A* Algorithm : explain what it is


## Todo 
* Depth First Search(DFS)
* Breath First Search(BFS)
* Dijkstra's Algorithm

# Inspiration
This project is inspirted by numerous pathfinding visualization projects on Youtube. Besides updating on more pathfinding algorithms mentioned in Todo, in the furture I could update and customize weights between nodes to more closely reflect real world mapping system. 

