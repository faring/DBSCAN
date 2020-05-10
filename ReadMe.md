
# DBSCAN: A Density-based Spatial Clustering of Applications with Noise

Clustering is an unsupervised learning algorithm that divides the dataset into meaningful groups called clusters. The goal is to minimize intra-cluster differences and maximize inter-cluster differences. As the clustering of dataset depends on the type of application, there are a number of categories of clustering algorithms, such as partitional, hierarchical, density-based and grid-based clustering. 

In density-based clustering technique, clusters are dense regions in a space that is separated by regions of lower density. Here, a dense cluster is a density connected region in space, i.e. the density of points in that region is greater than a threshold. As the size of a cluster can grow based on the dense connectivity, density-based technique discovers clusters of arbitrary shape which is important for a spatial data clustering.

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. DBSCAN algorithm is designed to discover clusters of arbitrary shapes in large scale spatial datasets with noise based on the notion of neighbor’s density. Here, density-based notion means that a cluster consists of a maximal set of density connected points, i.e. spatially connected points. You can check the following paper to know more about DBSCAN.

M. Ester, H. P. Kriegel, J. Sander, X. A. Xu, "A Density-based Algorithm for Discovering Clusters in Large Spatial Databases with Noise", KDD, 1996, 96, 226–231.

# How to run the code:

(1) First, download and unzipped the folder and enter that folder. Then run the following command from a terminal to run the code: (Required dataset 'test.csv' should be in the same folder)

    $ python3 DBSCAN.py

(2) After running the program, you will see the following output in the console as Eps and MinPts already set to a fixed value. 

    INPUT:
    Tuples#: 300
    Eps: 2 
    MinPts: 5

    OUTPUT:
    cluster 0: 98 points
    cluster 1: 100 points
    cluster 2: 100 points
    Noise: 2 points
    
(3) The program will also 


Thank you!

# Contact:
Md. Mahbub Alam (emahbub.cse@gmail.com)
