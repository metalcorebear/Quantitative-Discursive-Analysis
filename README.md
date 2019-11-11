# Quantitaive Discursive Analysis

(C) 2019 Mark M. Bailey

## About
Quantitative Discursive Analysis (QDA) will convert bodies of text into mathematical graph objects built from noun phrases, where each noun or modifier becomes a vertex, and each edge is determined by how the nouns and vertexes are linked within phrases.  The more central the noun is to the overall text content, the higher the centrality measure of that particular noun.  Thus, the graph is a weighted representation of discursive content, making it more robust that simple keyword frequencies.  This object can be used to mathematically compare the discursive content of two or more bodies of text.  This is done by calculating the "resonance" between two bodies of text, where resonance is the cosine angle between the betweenness centralities of the intersection of all vertices.  This resonance value is normalized between [0,1], where 0 indicates no discursive similarity, and 1 indicates perfect discursive similarity.

## Resonance in Series
When lists of discursive objects are generated, this tool can be used to measure the resonance in series, where resonance between object i and object i+1 is measured throughout the entire series.  This feature can be useful in measuring time series resonance, for example, discursive similarity of aggregated news over time.

## Discursive Communities
This tool can also be used to generate discursive communities.  When a list of discursive objects are generated, a weighted association matrix and associated graph (with edge weights representing resonance) can be generated, as well as its weighted betweenness centralities (indicating the relative importance of each discursive object within the network).  This feature can be useful for community identification on social media, where disursive similarity is used as a measure of connection (more robust than simply being "friended," "followed," or "liked").

## More information
This tool is built on NetworkX and TextBlob.  Please see relevant documentation for additional information on what other calculations can be done on NetworkX graph objects generated using this library.

## Download
https://pypi.org/project/QDA/

## Sample Usage

import QDA

*#Instantiate discursive object.*  

text_graph = QDA.discursive_object('This is a string of your text.  For best results, this string should be at least as long as a typical news article.')  


*#Return list of noun phrases.*  

#Reuturns a list of tuples.  

text_graph.nouns  


*#Return graph object.*  

#Returns a NetworkX graph object.  

text_graph.graph  


*#Return dictionary of betweenness centrality measurements.*  

text_graph.spectrum  


*#Calculate resonance between two discursive objects.*  

#Returns a float.  

a = QDA.resonate(text_graph_1, text_graph_2)  


*#Calcuate resonance in series from a list of discursive objects.*  

#G_list is a list of discursive objects.  

#Returns a dictionary  

resonance_series = QDA.resonate_as_series(G_list)  


*#Instantiate a discursive community from a list of discursive objects.*  

#G_list is a list of discursive objects.  

d_community = QDA.discursive_community(G_list)  


*#Return weighted association matrix.*  

#Returns Numpy array.  

d_community.A  


*#Return community graph object.*  

#Returns NetworkX graph object.  

d_community.G  


*#Return community betweenness centrality dictionary.*  

d_community.spectrum  