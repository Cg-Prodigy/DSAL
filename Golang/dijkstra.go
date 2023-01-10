package main

import (
	"fmt"
	"math"
)

type Path map[string]map[string]float64

func (p Path) djAlgorithm(start, end string) map[string]float64{
	distances:=make(map[string]float64,len(p))
	unvisted:=[]string{}
	visited:=[]string{}
	// populate univisted with all the available nodes
	for key,_:=range p{
		unvisted=append(unvisted, key)
		if key==start{
			distances[key]=0
		}else{
			distances[key]=math.Inf(0)
		}
	}
	for{
		start_node:=p[start]
		if checkPresence(visited,start){
			for key,val:= range start_node{
				cost:=val+distances[start]
				if cost<distances[key]{
					distances[key]=cost
				}
			}
			visited=append(visited, start)
			unvisted=popSlice(unvisted,start)
			start=minimumCost(distances,unvisted)
		}
		if start==end{
			break
		}
	}
	return distances
}

// function to check presence of an element in an array
func checkPresence(arr []string, s string)bool{
	for _,val:=range arr{
		if val==s{
			return false
		}
	}
	return true
}
// function to find the minimum cost
func minimumCost(d map[string]float64,s []string) string{
	node:=""
	value:=math.Inf(0)
	for _,v:=range s{
		if d[v]<value{
			node=v
		}
	}
	return node
}
// function to remove an element in a list
func popSlice(s []string,e string) []string{
	slice_copy:=[]string{}
	for _,val:=range s{
		if val==e{
			continue
		}else{
			slice_copy=append(slice_copy, val)
		}
	}
	return slice_copy
}

func main(){
	path:=Path{
        "A":{"B":2,"C":4},
        "B":{"A":2,"C":3,"D":8},
        "C":{"A":4,"E":5,"D":2,"B":3},
        "D":{"B":8,"C":2,"E":11,"F":22},
        "E":{"C":5,"D":11,"F":1},
        "F":{"E":1,"D":22},
    }
	start:="A"
	end:="F"
	cost:=path.djAlgorithm(start,end)
	fmt.Println(cost)
}