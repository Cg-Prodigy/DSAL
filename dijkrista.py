# Ego kipkemei Brian
# Dec - 6th - 2022
# Dijkrista Algorithm

def algorithm(start,end,path:dict):
    unvisited=[key for key in path.keys()]
    visited=[]
    value=lambda x: 0 if x==start else float("inf")
    shortest_distance={key:[value(key),{"prev_node":""}] for key in path.keys()}
    while True:
        if start not in visited:
            start_node=path[start]
            for key in start_node.keys():
                cost=start_node[key]+shortest_distance[start][0]
                if cost<shortest_distance[key][0]:
                    shortest_distance[key][0]=cost
                    shortest_distance[key][-1]["prev_node"]=start
            visited.append(unvisited.pop(unvisited.index(start)))
            start=minimum_cost(shortest_distance,unvisited)
        if not unvisited:
            break
    s_path,s_distance=reconstruct(shortest_distance,start,end)
    return f"Shortest Path:{s_path}\nTotal Distance:{s_distance}"

def reconstruct(dct:dict,st,end):
    path=[end]
    t_distance=dct[end][0]
    start=dct[end][-1]["prev_node"]
    while True:
        path.append(start)
        start=dct[start][-1]["prev_node"]
        if start==st:
            break
    path.reverse()
    return path,t_distance
def minimum_cost(dct:dict,lst:list):
    start=float("inf")
    s_key=''
    for elem in lst:
        cost=dct[elem][0]
        if cost<start:
            start=cost
            s_key=elem
    return s_key

if __name__=="__main__":
    path={
        "A":{"B":2,"C":4},
        "B":{"A":2,"C":3,"D":8},
        "C":{"A":4,"E":5,"D":2,"B":3},
        "D":{"B":8,"C":2,"E":11,"F":22},
        "E":{"C":5,"D":11,"F":1},
        "F":{"E":1,"D":22}
    }
    # path={
    #     "A":{"B":2,"D":8},
    #     "B":{"A":2,"D":5,"E":6},
    #     "D":{"A":8,"B":5,"E":3,"F":2},
    #     "E":{"B":6,"D":3,"F":1,"C":9},
    #     "F":{"D":2,"E":1,"C":3},
    #     "C":{"F":3,"E":9}
    # }
    print(algorithm("A","F",path))