#!/usr/bin/env python
"""
@author: metalcorebear
"""

#Calculates discursive similarity (cosine angle) between bodies of text.
#Library is built on NetworkX and Textblob.

import networkx as nx
from textblob import TextBlob
import re
import numpy as np


#Calculate resonance between two discursive objects.
def resonate(G1, G2):
    G1_nodes = list(G1.spectrum.keys())
    G2_nodes = list(G2.spectrum.keys())
    G_intersect = list(set(G1_nodes) & set(G2_nodes))
    if len(G_intersect) != 0:
        G1_list = [G1.spectrum[node] for node in G_intersect]
        G2_list = [G2.spectrum[node] for node in G_intersect]
        G1_vector = np.array(G1_list)
        G2_vector = np.array(G2_list)
        G1_norm = np.linalg.norm(G1_vector)
        G2_norm = np.linalg.norm(G2_vector)
        if G1_norm*G2_norm == 0.0:
            resonance = 0.0
        else:
            dot_prod = np.dot(G1_vector, G2_vector)
            resonance = dot_prod/(G1_norm*G2_norm)
    else:
        resonance = 0.0
    return resonance

#Resonate list of discursive objects
def resonate_as_series(G_list):
    resonance_series = []
    resonance_keys = list(range(len(G_list)-1))
    for i in range(len(G_list)-1):
        a = resonate(G_list[i], G_list[i+1])
        resonance_series.append(a)
    resonance_series_dict = dict(zip(resonance_keys, resonance_series))
    return resonance_series_dict


def resonate_as_matrix(G_list):
    n = len(G_list)
    A = np.zeros((n,n))
    ji_list = []
    for i in range(n):
        for j in range(n):
            if i != j:
                if (j,i) not in ji_list:
                    A[i][j] = resonate(G_list[i],G_list[j])
                    ji_list.append((j,i))
    return A

#The following functions build the discursive object.
def get_nouns(text):
    text = text.lower()
    text = re.sub(r'[^\x00-\x7f]',r'', text)
    new_text = re.sub(r'\d+', '', text)
    new_text = re.sub(r'\n', ' ', new_text)
    punctuations = '!()-[]{};:"\,<>./?@#$%^&*_~'
    new_text = new_text.strip(punctuations)
    #new_text = new_text.translate(string.maketrans("",""), string.punctuation)
    new_text = new_text.strip()
    new_text = new_text.strip("'")
    blob = TextBlob(new_text)
    nouns = blob.noun_phrases
    return nouns

def get_edges(nouns):
    phrase_edges = []
    for phrase in nouns:
        phrase = phrase.split()
        phrase_mirror = phrase
        for i in range(len(phrase)):
            for j in range(len(phrase_mirror)):
                if i != j:
                    edge = (phrase[i], phrase_mirror[j])
                    phrase_edges.append(edge)
    return phrase_edges

def get_nodes(edges):
    noun_str = ''
    for edge in edges:
        for word in edge:
            noun_str += word
            noun_str += ' '
    noun_list = noun_str.split()
    noun_set = set(noun_list)
    phrase_nodes = list(noun_set)
    return phrase_nodes

def build_graph(phrase_nodes, phrase_edges):
    G = nx.MultiGraph()
    G.add_nodes_from(phrase_nodes)
    G.add_edges_from(phrase_edges)
    return G

def spectrum(G):
    centrality = nx.betweenness_centrality(G)
    return centrality

class discursive_object:
    
    """Builds a discursive object from a body of text."""
    
    def __init__(self, text):
        self.nouns = get_nouns(text)
        edges = get_edges(self.nouns)
        nodes = get_nodes(edges)
        self.graph = build_graph(nodes, edges)
        self.spectrum = spectrum(self.graph)

class discursive_community:
    
    """Builds a discursive community from a list of discursive objects."""
    
    def __init__(self, G_list):
        self.A = resonate_as_matrix(G_list)
        self.G = nx.from_numpy_matrix(self.A)
        self.spectrum = nx.betweenness_centrality(self.G, weight='weight')