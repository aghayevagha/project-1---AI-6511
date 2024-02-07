# Project 1 - Water pitchers

## Problem description
You are given a text file with 2 lines. First line has a variable number of integers, comma
separated and Second line has an integer

Input File Structure:
 input.txt <br>
```
1,4,10,15,22 // pitchers
181 // target quantity 
```
<br> We are required to find the minimum number of operations to have target quantity of water on the "virtual" pitcher by using A* algorithm.

## Solution
A*, a widely used algorithm in pathfinding and graph traversal, combines the advantages of both uniform-cost search and greedy best-first search algorithms. It efficiently finds the shortest path in a weighted graph, where the cost of reaching a node is evaluated based on the sum of two functions:

  - Heuristic function (h): This function estimates the cost from the current state to the goal state, in our case it is calculated as the difference of target water and current quantity of water on our virtual picher

  - Cost function (g): This function represents the actual cost from the start node to the current node. In our case, each operation: either filling or emptying the picher is 1 regardless its capacity.

Everytime we change water quantity on pichers our cost increases by one, and in case of moving water to the virtual infinite picher, our heuristic function decreases by exactly the quantity.

## How to run
Download the project with following commands
```
# Clone the repo
git clone https://github.com/aghayevagha/project-1---AI-6511/)https://github.com/aghayevagha/project-1---AI-6511/

#enter the project
cd waterpitcher

#run the agent file
python3 src/agent.py
```
