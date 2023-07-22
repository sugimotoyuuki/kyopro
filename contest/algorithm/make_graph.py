import matplotlib.pyplot as plt
import networkx as nx

n1, n2, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

G = nx.Graph()
G.add_edges_from(ab)
nx.draw(G, with_labels=True)
plt.show()
