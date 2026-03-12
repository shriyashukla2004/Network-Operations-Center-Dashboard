import streamlit as st
from pyvis.network import Network
from topology import build_topology

st.title("🌐 Network Topology")

G = build_topology()

net = Network(height="500px", width="100%")

for node in G.nodes:
    net.add_node(node, color="#00C8FF", size=20)

for edge in G.edges:
    net.add_edge(edge[0], edge[1])

net.save_graph("topology.html")

with open("topology.html","r",encoding="utf-8") as f:
    st.components.v1.html(f.read(),height=500)