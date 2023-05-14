# This is an extra class besides the interface class, the difference between is
# that when you run the interface class it will let you deal with program by
# using a GUI unlike main class which will let you deal with the program on console.

import Algorithms


# return the graph after reading the nodes and the edges from cities.txt file.
def buildGraph():
    graphs = {}
    file = open('cities.txt', 'r')
    cnt = 0
    for line in file:
        data = line.split(" ")
        if int(data[0]) not in graphs.keys():
            graphs[cnt] = [[int(data[1]), int(data[2])]]
            cnt += 1
        else:
            graphs[int(data[0])].append([int(data[1]), int(data[2])])
    return graphs


# return the heuristics values based on the start node.
def heuristic(cityNum):
    # __,__ Areal, Walking
    cnt = 0
    ar = {}
    walk = {}
    data = open('heuristic.txt', 'r')
    for num, line in enumerate(data):
        if num == cityNum:
            temp = line.strip().split('/')
            for values in temp:
                nums = values.split(',')
                ar[cnt] = int(nums[0])
                walk[cnt] = int(nums[1])
                cnt += 1
            break
    return ar, walk


def menu():
    print(
        "Algorithms:\n(1)BFS\n(2)DFS\n(3)A*\n(4)BFS with two goals\n(5)DFS with two goals\n"
        "(6)A* (Walking --> Aerial)\n(7)Exit")


if __name__ == "__main__":
    graph = buildGraph()
    lst = [1, 2, 3, 4, 5, 6, 7]
    while True:
        menu()
        chose = int(input("Enter selection: "))
        print("------------------------------------")
        while chose not in lst:
            chose = int(input("Enter selection: "))
        if chose == 1:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            Algorithms.bfs(graph, start, goal)
            print("------------------------------------")
        elif chose == 2:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            Algorithms.dfs(graph, start, goal)
            print("------------------------------------")

        elif chose == 3:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            aerial, walking = heuristic(start)
            heu = int(input("Enter (1) for aerial heuristic or (2) for walking heuristic: "))
            while heu not in [1, 2]:
                heu = int(input("Enter selection: "))
            if heu == 1:
                Algorithms.AStar(graph, aerial, start, goal)
            else:
                Algorithms.AStar(graph, walking, start, goal)
            print("------------------------------------")

        elif chose == 4:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            goal2 = int(input("Enter second goal node: "))
            Algorithms.bfs(graph, start, goal, goal2)
            print("------------------------------------")

        elif chose == 5:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            goal2 = int(input("Enter second goal node: "))
            Algorithms.dfs(graph, start, goal, goal2)
            print("------------------------------------")

        elif chose == 6:
            start = int(input("Enter start node: "))
            goal = int(input("Enter goal node: "))
            Algorithms.AStarWA(graph, heuristic(start), start, goal)
            print("------------------------------------")

        else:
            exit(1)
