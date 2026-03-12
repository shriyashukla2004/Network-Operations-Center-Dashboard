import networkx as nx

def build_topology():

    G = nx.Graph()

    edges = [
        ("Router", "Server1"),
        ("Router", "Server2"),
        ("Router", "GoogleDNS"),
        ("Router", "CloudflareDNS")
    ]

    G.add_edges_from(edges)

    return G