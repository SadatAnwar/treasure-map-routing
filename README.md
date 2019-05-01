# Treasure Map Routing

## Solution Description
### Problem 1: Find the shortest path

The treasure map can be considered as a graph, where we have nodes, and the roads are connections (edges) between the
nodes. Since traveling from one node, to the next, always takes 5 minutes, the edges of the graph have uniform weight.
The shortest path, is then the path with the least amount of nodes. 

A simple way to solve this is by using the Breadth First Search. We essentially "search" for the destination (treasure)
node, and keep track of all the nodes that we visit on the path to the destination. Once we reach the destination, we
can back-track our steps to make the path. 

### Problem 2: Dragons
Since it takes 5 minutes from node to node, and a dragon sneezes every 15 mins, we need to make sure that we are not on 
a dragon node at time t where t is a multiple of 3 `t=3,6,9,....`. This means that our path should not contain a dragon
node at any index in t. 

For this solution, we can try and find all the possible paths from the start till the finish. Once we have all possible 
paths, we want to find the shortest one, that meets the above criteria.

There are 3 possibilities:
1. The shortest path, already fulfills the above criteria.
    * We simply accept this as the answer

2. The shortest path contains a dragon node at any index that is multiple of 3.
    * If the path contains dragons at 3 consecutive nodes of the path eg: Path= [1,2,3,4,5,6] Dragons=(3,4,5)
    then there is no way this can lead to a valid path and we skip it

3. Else we can circle the nodes before the dragon to allow crossing the dragon when he is not sneezing.
    eg `path: 0->1->2->3->4` and given dragon at 3. A possible solution would be `[0->1->2->1->2-3->4]` by circling over 
    1 and 2 we delayed reaching 3 by 10 mins, so instead of reaching 3 at 15, we reach at 25, avoiding the burn.
    * We then update all paths that have a potential of getting burnt with a possible path that wont, and then 
    find the shortest path (See [get_treasure_avoiding_dragons](src/treasure_finder.py#L27))
    
### Problem 3: Annoying neighbour.

For Problem 3, we are asked to avoid the roads taken by the neighbour. Its also said that the neighbour will always take
the shortest path. For this we can first find the shortest path and know what path the neighbour will take.
Once we know that, we simply update the graph, and remove the roads taken by the neighbour and compute the 
shortest path for this updated graph. This will give us the shortest path avoiding the roads taken by out neighbour.



## Solution execution
I have implemented the solution in python for a single reasons: **The setup was provided in python, it was easy to get started, and I could reuse ALL of the provided code.**

The project uses python types to give much nicer function definitions and also enable to IDE to assist and help with 
code completion. You will therefore need at least python 3.6 (Docker image uses python 3.7). 

The unittests present in [test folder](test)

To simplify the sharing of the project, the project has a [Dockerfile](Dockerfile) that sets up the execution in a docker
container. The docker build also runs the tests at build time. 

Easiest way to run is execute the `docker_run.sh` file located at the root of the project. This script builds and runs
the routing container with all the necessary parameters (to share volume)

