import networkx as nx
import matplotlib.pyplot as plt

cities = [
]


# Plot the nodes and the edges between using different libraries (networkx and matplotlib)
def plotGraph(graph, optimalPath):
    G = nx.Graph()
    for i in range(0, list(graph.keys())[-1]): # You did an edit here list(graph.keys())[-1]
        G.add_node(i)

    for key, item in graph.items():
        for node in item:
            G.add_edge(key, node[0], color='r', weight=1, label=node[1])

    for i in range(len(optimalPath) - 1):
        G.add_edge(optimalPath[i], optimalPath[i + 1], color='g', weight=3)

    edgesColor = nx.get_edge_attributes(G, 'color').values()
    edgesWeight = nx.get_edge_attributes(G, 'weight').values()

    color_map = []
    # coloring the nodes based on the optimal path.
    for node in G:
        if node in optimalPath:
            color_map.append('Green')
        else:
            color_map.append('Red')

    # change nodes from numbers to names
    mapping = {0: "Aka", 1: "Bethlehem", 2: "Dura", 3: "Haifa", 4: "Halhoul", 5: "Hebron", 6: "Jenin", 7: "Jericho",
               8: "Jerusalem", 9: "Nablus",
               10: "Nazareth", 11: "Qalqilya", 12: "Ramallah", 13: "Ramleh", 14: "Sabastia", 15: "Safad", 16: "Salfit",
               17: "Tubas", 18: "Tulkarm", 19: "Yafa"}
    G = nx.relabel_nodes(G, mapping)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, edge_color=edgesColor, width=list(edgesWeight),
            node_color=color_map)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
    plt.show()
