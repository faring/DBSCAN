#=======================================================================#
# DBSCAN: A Density-based Spatial Clustering of Applications with Noise #
# Author: Md Mahbub Alam                                                #  
# Email: emahbub.cse@gmail.com                                          #
#=======================================================================#

import math
import matplotlib.pyplot as plt 
import random
import datetime as dt
import utm

visited = list()
clusters = dict()
noise = list()

#Read dataset from file and creates a list of tuples 
#tuple(lat, lon)
def ReadDataset(fileName):
	try:
		in_file_ptr = open(fileName, 'r')
	except:
		print('\nThere is no file named \'' + fileName + '\', Please check the file path.\n')
	else:
		dataset = list()
		in_file_ptr.readline()
		for line in in_file_ptr:
			dataset.append(tuple(map(float, line.strip().split(';'))))
		in_file_ptr.close()
		return dataset

#calculate and return Euclidean distance between two points
def EuclideanDistance(p1, p2):
	return math.sqrt(pow((p2[0]-p1[0]), 2) + pow((p2[1]-p1[1]), 2))

#check whether a point already is in a cluster or not
def IsInCluster(point):
	for cluster in clusters.values():
		if(point in cluster):
			return True
	return False

#return Eps-neighborhood of a point
#these neighbors are directly density-reachable neighbor
def GetNeighbors(dataset, point1, eps):
	neighbors = list()
	for point2 in dataset:
		if(point1 == point2):
			continue
		dist = EuclideanDistance(point1, point2)
		if(dist <= eps):
			neighbors.append(point2)
	return neighbors

#Expand Eps-neighborhood for each current neighbors
#Find density-reachable neighbors from directly density-reachable neighbors
def ExpandNeighborhood(dataset, neighbors, eps, minPts, currentCluster):
	for point in neighbors:
		if(point not in visited):
			visited.append(point)
			
			newNeighbors = GetNeighbors(dataset, point, eps)
			#print('New Neighbors:', len(newNeighbors))

			if(len(newNeighbors) >= minPts): #core point
				for nPoint in newNeighbors:
					if(nPoint not in neighbors):
						neighbors.append(nPoint)
		
		if(not IsInCluster(point)): #border point
			if(point not in currentCluster):
				currentCluster.append(point)
	
#DBSCAN Algorithm
#dataset: A dataset containing n objects
#eps: Maximum radius of the neighborhood(spatial threshold)
#minPts: Minimum number of points within eps-neighborhood
def DBSCAN(dataset, eps, minPts):
	cid = 0 #cluster id
	for point in dataset:
		if(point not in visited):
			visited.append(point) 

			neighbors = GetNeighbors(dataset, point, eps)
			#print('Neighbors:', len(neighbors))

			if(len(neighbors) >= minPts): #core point
				currentCluster = list()
				currentCluster.append(point)
				ExpandNeighborhood(dataset, neighbors, eps, minPts, currentCluster)
				# print(len(currentCluster))
				clusters[cid] = currentCluster
				cid += 1
			else: #noise/outlier
				noise.append(point)

#Print cluster and noise infomration
def PrintClusterDetails(clusters, noise):
    for cid, cluster in clusters.items():
        print('cluster ' + str(cid) + ': ' + str(len(cluster)) + ' points')
    print('Noise: ' + str(len(noise)) + ' points')

#plot clusters and noise points
def PlotClusters(clusters, noise):
	for cluster in clusters.values():
		colorCode = '#{:06x}'.format(random.randint(0, 256**3)) #idea: StackOverflow
		for point in cluster:
			plt.plot(point[0], point[1], marker = 'o', color = colorCode)

	for point in noise:
		plt.plot(point[0], point[1], marker = 'x', color = 'red')

	plt.title('Algorithm: DBSCAN' + '  #Cluster: ' + str(len(clusters)) + 
			  '  Noise Points: ' + str(len(noise)))
	plt.show()

#starting point of the program
def Start():
	dataset = ReadDataset('test.csv')
	
	eps = 2 
	minPts = 5 

	print('\nINPUT:')
	print('Tuples#:', len(dataset))
	print('Eps:', eps, '\nMinPts:', minPts)
	
	DBSCAN(dataset, eps, minPts)
	
	print('\nOUTPUT:')
	DBSCAN(dataset, eps, minPts)
	PrintClusterDetails(clusters, noise)
	PlotClusters(clusters, noise)
	print('\n')

#main function
if __name__ == "__main__":
    Start()
