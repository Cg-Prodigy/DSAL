class Dijkstra:
    """
    Example of how the path should look
    path={
        "A":{"B":2,"C":4},
        "B":{"A":2,"C":3,"D":8},
        "C":{"A":4,"E":5,"D":2,"B":3},
        "D":{"B":8,"C":2,"E":11,"F":22},
        "E":{"C":5,"D":11,"F":1},
        "F":{"E":1,"D":22}
    }
    """
    def __init__(self,start_node,end_node,path:dict) -> None:
        self.path=path
        self.start_node=start_node
        self.end_node=end_node
        self.visited=[]
        self.value=lambda x:0 if x==self.start_node else float("inf")
        self.shortest_distance={key:[self.value(key),{"prev_node":""}] for key in self.path.keys()}
        self.unvisited=[key for key in self.path.keys()]
    def shortest_path(self):
        """
        Finds the shortest path with the help of the two functions minimum_value and reconstruct.
        Returns a tuple containing the shortest distance and the total shortest distance.
        """
        while True:
            start=self.path[self.start_node]
            if start not in self.visited:
                for key in start.keys():
                    cost=self.shortest_distance[self.start_node][0]+start[key]
                    if cost<self.shortest_distance[key][0]:
                        self.shortest_distance[key][0]=cost
                        self.shortest_distance[key][-1]["prev_node"]=self.start_node
                self.visited.append(self.unvisited.pop(self.unvisited.index(self.start_node)))
                self.start_node=self.minimum_value(self.shortest_distance,self.unvisited)
            if self.start_node==self.end_node:
                break
        return self.reconstruct(self.shortest_distance,self.end_node)
    def minimum_value(self,path:dict,lst:list):
        value=float("inf")
        key=None
        for elem in lst:
            if path[elem][0]<value:
                value=path[elem][0]
                key=elem
        return key
    def reconstruct(self,dct:dict,end) -> tuple:
        path=[end]
        start=dct[end][-1]["prev_node"]
        while True:
            path.append(start)
            start=dct[start][-1]["prev_node"]
            if not start:
                break
        path.reverse()
        return path,dct[end][0]

    def __str__(self) -> str:
        return "Implementation of Dijkstra Algorithm"