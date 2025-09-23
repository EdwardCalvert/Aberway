The code for the Aberway hackathon.

## Task
Participants are tasked with finding a path when given a starting position, some nodes that the path must cross through, and the length of the path. From that, the participants must find the path that starts at the starting position, goes through the given nodes, and ends on a node. Fastest wins.

### Example A
A Delivery Person (referred to as “DP” from now on) at the Post Office at node 0. DP has a few mandatory packages to deliver that need to be delivered today, those are at nodes 10, 11, and 14. DP’s van only has 676.75 ±0.06 fuel. It is important that DP runs out of fuel at a Place where DP can stop (any node) so that DP can refill the van’s fuel with a fuel canister, so DP can not stop in the middle of the road. Find the path that DP must take, and where DP will have to refuel.

**Values:**

Start Position: 0 

List of nodes their path must cross: `[10,11,14]`

Length (AKA Final weight): 676.75 ±0.06

Correct answer: `0, 2, 10, 13, 11, 14, 15`

### Example B
Jack (referred to as “J” from now on) is going to go on a run, J will travel 758.97 ±0.06 far. J wants to pass by a street newspaper seller at node 34, J also wants to pass by his favourite ice cream shop at node 27, and run past the dog park at 17. J is self conscious and has to stop running at a node not in the middle of a road. Find the path that J must take, and where J will finish his run.

**Values:**

Start Position: 29

List of nodes their path must cross: `[34, 27, 17] `

Length (AKA Final weight): `758.97 ±0.06`

Correct Answer: `29, 33, 34, 27, 18, 17, 10`


### Example C
An ice cream van (referred to as “ICV'' from now on) starts at node 53, ICV has 1038.42 ±0.07 fuel and wants to stop by some parks at nodes 54, 51, 38, and 36. What path should ICV take to make sure it runs out of fuel at a node?

**Values:**
Start Position: 53

List of nodes their path must cross: `[54, 51, 38, 36]`

Length (AKA Final weight): `1038.42 ±0.07`

Correct answer: `53, 54, 51, 41, 38, 37, 36, 43`

### Example D
A Police Officer in a car (referred to as “PO” from now on) starts at the police station at 47. PO has to meet the quota of travelling 2044.79 ±0.14. PO needs to make sure nodes 34, 19, 0,  and 12 are safe. When PO finishes their route, they need to stop and contact the police station, so PO must stop on a Node. What path will the POtake? And What node will PO end on?

**Values:**

Start Position: 47

List of nodes their path must cross: `[34, 19, 0, 12]` 

Length (AKA Final weight): `2044.79 ±0.14`

Correct answer: `47, 45, 43, 42, 37, 34, 27, 26, 19 ,9, 3, 0 ,2, 11, 12`


## Getting started:

To get started, for the repository and edit the `Your_Name_Aberway.py` file. 

## FAQ:

How do we know that there will only be one path?

We don’t necessarily know that there will only be one path, but there is a negligible chance that there are two paths that start from that given node, pass through the other mandatory nodes, are both the given length to two decimal places (even with the error), and both end on a node.

Are the example locations correct?

The locations are not necessarily what they are claimed to be by the examples.

What is the random seed?

`random.seed(a=0x5326478324724367635627432857846378)`

### Resources:
Base map

![alt text](map.png)
Inverted Base map

![alt text 2](mapI.png)

Map with the node numbers

![alt text 3](mapWithNodeNumbers.png)

# Base Code
The basecode can be found in the `YourName__AberWay.py` file.
Visualising Graphs - Gephi:
https://gephi.org/users/

Github Documentation:
https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop

