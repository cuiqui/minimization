from collections import defaultdict


class DSU:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    def subsets(self) -> list[set]:
        groups = defaultdict(set)
        for x in self.parent:
            root = self.find(x)
            groups[root].add(x)
        return list(groups.values())

    def __getitem__(self, key) -> set:
        root = self.find(key)
        return {x for x in self.parent if self.find(x) == root}
