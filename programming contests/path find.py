from collections import defaultdict 
class Graph(): 

        def __init__(self,vertices): 
                self.V= vertices      	
                self.graph = defaultdict(list) 
                self.paths = []
                self.all_vists = []
        def add_edge(self,u,v): 
                self.graph[u].append(v)
                
        def recursive_path_finder(self, u, d, f, visited, path): 

                visited[u]= True
                self.all_vists[u]= True
                path.append(u)
                if u == d:
                        a = path
                        paths.append(a) # This should be more general
                                                # Because sometimes no worky
                else: 
                        for i in self.graph[u]: 
                                if visited[i]==False: 
                                        self.recursive_path_finder(i, d, f+1, visited, path[f-1:]) 
					
                visited[u]= False

        def find_paths(self,s, d):

                visited =[False]*(self.V)
                self.all_vists = [False]*(self.V)

                path = []
                
                self.recursive_path_finder(s, d,0, visited, path)

paths = []

_input = input()
_input = _input.split(' ')
n=int(_input[0])
p=int(_input[1])
s=int(_input[2])
e=int(_input[3])

g = Graph(n)
for i in range(p):
    link = input().split(' ')
    g.add_edge(int(link[0]), int(link[1]))
    g.add_edge(int(link[1]), int(link[0]))

g.find_paths(s,e)

print(len(min(paths)))

