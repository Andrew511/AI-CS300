from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean,infinity


class ManhattenGraphProblem(GraphProblem):
    def h(self, node):
        "h function is Manhatten distance from a node's state to goal."
        locs = getattr(self.graph, 'locations', None)
        if locs:
            return manhatten(locs[node.state], locs[self.goal])
        else:
            return infinity


def manhatten(a, b):
    '''The Manhatten distance between two (x, y) points.'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def readMazeFromFile(fileName):
    matrix = {}
    i = 0
    start = (0, 0)
    goal = (0, 0)
    with open(fileName) as f:
        start = tuple(map(int, f.readline().rstrip('\n').strip('()').split(',')))
        goal = tuple(map(int, f.readline().rstrip('\n').strip('()').split(',')))
        for line in f.readlines():
            line = line.rstrip('\n')
            j = 0
            for cost in line:
                if int(cost) != 0:
                    matrix[(j, i)] = int(cost)
                j = j + 1
            i = i + 1
    graph = Dict()
    for point in matrix.keys():
        entry = {point: {}}
        child1 = None
        child2 = None
        try:
            child1 = {(point[0], point[1] + 1): matrix[(point[0], point[1] + 1)]}
        except KeyError:
            pass
        try:
            child2 = {(point[0] + 1, point[1]): matrix[(point[0] + 1, point[1])]}
        except KeyError:
            pass
        if child1 is not None:
            entry[point].update(child1)
        if child2 is not None:
            entry[point].update(child2)

        graph.update(entry)
    undirGraph = UndirectedGraph(graph)
    undirGraph.locations = Dict()
    for i in undirGraph.nodes():
        undirGraph.locations.update({i: i})
    graphProblem = ManhattenGraphProblem(start, goal, undirGraph)
    return graphProblem


def main():
    firstGraphProblem = readMazeFromFile('L1.txt')
    secondGraphProblem = readMazeFromFile('L2.txt')
    thirdGraphProblem = readMazeFromFile('L3.txt')

    compare_searchers(problems=[firstGraphProblem, secondGraphProblem, thirdGraphProblem],
                      header=['Algorithm', 'L1.txt', 'L2.txt', 'L3.txt'],
                      searchers=[uniform_cost_search, greedy_best_first_graph_search, astar_search])


main()
