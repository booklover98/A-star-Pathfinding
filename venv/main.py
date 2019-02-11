import osmnx as ox 
import numpy as np 
import networkx as nx 
from sklearn.neighbors import KDTree 
import folium
import matplotlib.pyplot as plt 

oshawa = (43.945403, -78.892466)
G = ox.graph_from_point(oshawa, distance=2000)

# plot the graph
# ox.plot_graph(G, fig_height=10, fig_width=10, edge_color='black')

route = nx.shortest_path(G, np.random.choice(G.nodes), np.random.choice(G.nodes))
# plot a random route
# ox.plot_graph_route(G, route, fig_height=10, fig_width=10)

uoit = ox.geocode('2000 Simcoe St N, Oshawa, Ontario')
address = ox.geocode('18 Niagara Dr, Oshawa, Ontario')


# show both geocodes on map
fig, ax = ox.plot_graph(G, fig_height=10, fig_width=10, show=False, close=False, edge_color='black')
ax.scatter(uoit[1], uoit[0], c='red', s=100)
ax.scatter(address[1], address[0], c='blue', s=100)
# plt.show()

#
nodes, _ = ox.graph_to_gdfs(G)
nodes.head()

tree = KDTree(nodes[['y', 'x']], metric='euclidean')

uoit_idx = tree.query([uoit], k=1, return_distance=False)[0]
address_idx = tree.query([address], k=1, return_distance=False)[0]

closest_node_uoit = nodes.iloc[uoit_idx].index.values[0]
closest_node_address = nodes.iloc[address_idx].index.values[0]

#plot graph with geocodes and nodes
fig, ac = ox.plot_graph(G, fig_height=10, fig_width=10, show=False, close=False, edge_color='black')
ax.scatter(uoit[1], uoit[0], c='red', s=100)
ax.scatter(address[1], address[0], c='blue', s=100)
ax.scatter(G.node[closest_node_address]['x'], G.node[closest_node_address]['y'], c='green', s=100)
ax.scatter(G.node[closest_node_uoit]['x'], G.node[closest_node_uoit]['y'], c='green', s=100)
plt.show()

# display route on graph
route = nx.shortest_path(G, closest_node_uoit, closest_node_address)
fig, ax = ox.plot_graph_route(G, route, fig_height=10, fig_width=10, show=False, close=False, edge_color='black', orig_dest_node_color='green', route_color='green')
ax.scatter(uoit[1], uoit[0], c='red', s=100)
ax.scatter(address[1], address[0], c='blue', s=100)

plt.show()

#plot using folium -- needs to be sent to html and opened in browser.
m = ox.plot_route_folium(G, route, route_color='green')
folium.Marker(location=uoit, icon=folium.Icon(color='red')).add_to(m)
folium.Marker(location=address, icon=folium.Icon(color='blue')).add_to(m)
m.save('data.html')