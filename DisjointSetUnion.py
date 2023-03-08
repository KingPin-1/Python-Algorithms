# Union Find Template --> Python by me
# for leetcode --> 1971

from typing import List

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return True
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        
        return False
    
    def find(self,u):
        if u == self.parent[u]:
            return u
        
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    ds = UnionFind(n)
    for u,v in edges:
        ds.union(u,v)
    # print(ds.parent,ds.size)
    return ds.union(source,destination)

if __name__ == "__main__":
    n = 6
    edges = [[0,1],[2,3],[4,5],[3,4],[1,2]]
    source = 0
    destination = 5
    print(validPath(n,edges,source,destination))
