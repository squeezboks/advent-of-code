import multiprocessing
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    P = {}

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        P[neighbor] = current_vertex
    return P, D

class Topomap:
    def __init__(self, data, ncol):
        self.data = data
        self.ncol = ncol
        self.nrow = len(data)//ncol

    @property
    def nval(self):
        return len(self.data)
    
    def neighbours(self, address):
        condition = ord(self.data[address]) + 2

        # west neighbour
        if address % self.ncol > 0:
            west = address - 1
            neighbour = self.data[west]
            if ord(neighbour) < condition:
               yield west
        
        # east neighbour
        if (address + 1) % self.ncol > 0:
            east = address + 1
            neighbour = self.data[east]
            if ord(neighbour) < condition:
                yield east
        
        # north neighbour
        if address - self.ncol > 0:
            north = address - self.ncol
            neighbour = self.data[north]
            if ord(neighbour) < condition:
                yield north
        
        # south neighbour
        if address + self.ncol < self.nval:
            south = address + self.ncol
            neighbour = self.data[south]
            if ord(neighbour) < condition:
                yield south

def parse_input(input):
    data = input.split()
    ncol = len(data[0])
    flat = "".join(data)
    start = flat.index('S')
    end = flat.index('E')
    data = flat.replace('S','a').replace('E','z')
    return data, ncol, start, end

def run_dijkstra(topomap, start, end):
    print(f' - evaluating dijkstra for {start} > {end}', flush=True)
    # initalize graph
    g = Graph(topomap.nval)
    # add edges
    for i in range(topomap.nval):
        for n in topomap.neighbours(i):
            g.add_edge(i,n,1)

    # run dijkstra
    _, D = dijkstra(g, start)

    return D[end]

def s1(data):
    # parse data
    data, ncol, start, end = parse_input(data)
    topomap = Topomap(data, ncol)

    # initalize graph
    g = Graph(topomap.nval)

    # add edges
    for i in range(topomap.nval):
        for n in topomap.neighbours(i):
            g.add_edge(i,n,1)

    _, D = dijkstra(g, start)
    return D[end]

def s2(data):
    # parse data
    data, ncol, _, end = parse_input(data)
    low_points = [index for index, char in enumerate(data) if char == 'a']
    topomap = Topomap(data, ncol)

    # check for low point and remove flatness
    start_points = []
    for point in low_points:
        n = "".join([f"{topomap.data[i]}" for i in topomap.neighbours(point)])
        if n != 'aaaa':
            start_points.append((topomap, point, end))
    
    with multiprocessing.Pool() as pool:
        paths = [result for result in pool.starmap(run_dijkstra, start_points)]
    return min(paths) 


# protect the entry point
if __name__ == '__main__':
    with open("./2022/day12/day12_data.txt") as f:
        data = f.read()
        print(f" s1: {s1(data)}")
    
    with open("./2022/day12/day12_data.txt") as f:
        data = f.read()
        print(f" s2: starting up...")
        print(f" s2: {s2(data)}")


    

