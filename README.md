# TSP_NYC

Problem description:
Given a set of delivery locations in New York City, a truck is tasked to visit them in some order to drop off goods. Minimize the total time taken by determining the most optimal visit order.

## Installation
Create virtual environment: `python -m venv <name_of_virtualenv>`

Windows: `.\<name_of_virtualenv>\Scripts\activate`

Mac/Linux: `source ./<name_of_virtualenv>/bin/activate`

Then, install the required packages using: `pip install -r requirements.txt`

## Proposed solution 

The first part of the solution uses Machine Learning to predict the time required to travel between any two delivery locations (using geographical coordinates). Our data will come from the [New York City Taxi Trip Duration dataset](https://www.kaggle.com/c/nyc-taxi-trip-duration/overview) on Kaggle. We will perform some data cleaning that will remove outliers. The ML model will use a form of gradient boosting using decision trees and will mostly be either Light GBM or XGBoost. We will evaluate and compare our results using RMSE.

After calculating the time required to travel between delivery locations, we can formulate this problem as the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (where we are given a set of vertices and a set of weighted edges between every pair of vertices. We are then asked to find the shortest path that visits each vertex exactly once and returns to the origin). We can establish a complete graph with the delivery locations as vertices and the time required to travel between them as edge weights. Note that TSP is NP-hard, which means the optimal solution cannot be determined within polynomial time. Thus, we will use a set of approximation algorithms (such as a minimum spanning tree-based heuristic and [Christofides algorithm](https://en.wikipedia.org/wiki/Christofides_algorithm)) to find an approximate solution to TSP, i.e. the minimum time required to visit all delivery locations exactly once. We can guarantee our minimum total time will be at most 1.5 times the optimal total time using Christofides algorithm. 

## Extensions
Here are some of our ideas that we will implement, if our main solution goes well and we have time: 
For the first part, we can add a [weather dataset](https://www.kaggle.com/mathijs/weather-data-in-new-york-city-2016) as a factor when predicting the time required to travel between delivery locations. Plus, we can also consider the number of trucks between our current location and the following delivery location. This addition could more accurately generate accurate edge weights by predicting potential traffic.
We can incorporate more parameters to our program, in addition to the delivery locations. For example, we can add the restriction that the truck may only visit a delivery location at certain times of the day. Alternatively, we can add weights to each delivery location which represent the amount of goods delivered to that location. This opens up a lot of possibilities, including adding a capacity to the truck or a time limit. 

