import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

def visualize_nearest_neighbors(terms, embeddings):
    """
    Visualize nearest neighbors in embedding space.
    
    Args:
    - terms (list of str): List of terms.
    - embeddings (dict): Dictionary of terms and their embeddings.
    """
    data = np.array([embeddings[term] for term in terms])
    distance_matrix = cosine_distances(data)
    nearest_neighbors = {}
    
    for idx, term in enumerate(terms):
        sorted_indices = np.argsort(distance_matrix[idx])
        nearest_neighbor = terms[sorted_indices[1]]
        nearest_neighbors[term] = nearest_neighbor

    G = nx.DiGraph()
    for term in terms:
        G.add_node(term)
    for term, neighbor in nearest_neighbors.items():
        G.add_edge(term, neighbor)
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='blue', arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    plt.title('Nearest Neighbors in Embedding Space')
    plt.axis('off')
    plt.show()
