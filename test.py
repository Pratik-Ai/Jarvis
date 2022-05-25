import queue


T = {'R':['A','B','C'],'A':['D','E'],'B':['F','G','H'],'C':['I','J']}
print(T)
visited = []
queue = []
def bfs(visited,T,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end="->")
        for n in T[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

print("followig is BFS")
bfs(visited,T,'R')