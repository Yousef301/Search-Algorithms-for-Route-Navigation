import copy

# This list will use to convert the cities from numbers to names.
cities = ["Aka", "Bethlehem", "Dura", "Haifa", "Halhoul", "Hebron", "Jenin", "Jericho", "Jerusalem", "Nablus",
          "Nazareth", "Qalqilya", "Ramallah", "Ramleh", "Sabastia", "Safad", "Salfit", "Tubas", "Tulkarm", "Yafa"
          ]


def getNeighbors(graph, v):
    return graph[v]


def AStar(graph, heuristics, start, goal):
    # openedNode contains the nodes has been visited but didn't exceed yet 'There children are not discovered',
    # visited set contains the node that has been visited and there children were discovered.
    openedNode = {start}
    visited = set([])

    costs = {start: 0}
    parents = {start: start}

    while len(openedNode) > 0:
        node = None

        # finding the node with the lowest value.
        for i in openedNode:
            if node is None or costs[i] + heuristics[i] < costs[node] + heuristics[node]:
                node = i

        if node is None:
            print('No path exist....')
            return None

        # if the current node is the goal then the function will start to reconstruct the path from it to start node.
        if node is goal:
            optimalPath = []

            while parents[node] != node:
                optimalPath.append(node)
                node = parents[node]

            optimalPath.append(start)
            optimalPath.reverse()
            tC = totalCost(graph, optimalPath)
            print(f'Path from {cities[start]} to {cities[goal]} was found: {numToCity(optimalPath)}, '
                  f'with total cost of {tC}km')
            return optimalPath, tC

        for (temp, weight) in getNeighbors(graph, node):
            if temp not in openedNode and temp not in visited:
                openedNode.add(temp)
                parents[temp] = node
                costs[temp] = costs[node] + weight

            else:
                if costs[temp] > costs[node] + weight:
                    costs[temp] = costs[node] + weight
                    parents[temp] = node

                    if temp in visited:
                        visited.remove(temp)
                        openedNode.add(temp)

        # remove temp from openedNode and add it to visited, because all the temp neighbors were inspected
        openedNode.remove(node)
        visited.add(node)

    # if there is no path between the two nodes then print -->
    print('Path does not exist!')
    return None


# This function is an A* algorithm were the cost is Walking distance and the heuristic is the aerial distance
def AStarWA(graph, heuristics, start, goal):
    gr = costWalking(graph, heuristics[1])
    return AStar(gr, heuristics[0], start, goal), gr


def bfs(graphs, start, *goal):
    cnt = 1
    visited = []
    queue = [[start]]
    gr = formatG(graphs)
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal[0]:
            if len(goal) == cnt:
                if cnt == 1:
                    return print(f"Path from {cities[start]} to {cities[goal[0]]} was found:: {numToCity(path)}"), path
            else:
                # if there is more than goal the function will be executed again
                cnt += 1
                print(f"Path from {cities[start]} to {cities[goal[0]]} was found: {numToCity(path)}")
                bfs(graphs, goal[0], goal[1])
        else:
            adjacent_nodes = gr.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)


def dfs(graphs, start, *goal):
    cnt = 1
    stack = [[start]]
    visited = []
    gr = formatG(graphs)
    while stack:
        path = stack.pop(0)
        node = path[-1]
        if node == goal[0]:
            if len(goal) == cnt:
                if cnt == 1:
                    return print(f"Path from {cities[start]} to {cities[goal[0]]} was found:: {numToCity(path)}"), path
            else:
                # if there is more than goal the function will be executed again
                cnt += 1
                print(f"Path from {cities[start]} to {cities[goal[0]]} was found: {numToCity(path)}")
                dfs(graphs, goal[0], goal[1])
        children = gr[node]
        for child in children:
            if child not in visited:
                newPath = path + [child]
                stack.insert(0, newPath)
                visited.append(child)


# formatG function used to return the graph in a specific view that will make it easier to use
# it in bfs and dfs functions
def formatG(graph):
    gr = copy.deepcopy(graph)
    cnt = 0
    for line in gr.values():
        nums = []
        for da in line:
            nums.append(da[0])
        gr[cnt] = nums
        cnt += 1
    return gr


# make the walking distance as the real cost in the graph
def costWalking(graph, walking):
    gr = copy.deepcopy(graph)
    for key, value in gr.items():
        for lst in value:
            lst[1] = walking[lst[0]]
    return gr


# return the cost of the optimal path
def totalCost(graph, path):
    tCost = 0
    for i in range(len(path) - 1):
        costs = graph[path[i]]
        for j in costs:
            if j[0] == path[i + 1]:
                tCost += j[1]
                break
    return tCost


# convert the cities from numbers to text "names"
def numToCity(path):
    lt = copy.deepcopy(path)
    for i in range(len(lt)):
        lt[i] = cities[lt[i]]
    return lt
