# For reading the dataset.csv file
import csv
import random
import math

# Function that returns the eucledian distance between two points having 
# co-ordinates (x1, y1) and (x2, y2) in the x-y plane
def eucledian_dist(point1, point2):
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]
  return math.sqrt( ( (x2 - x1) ** 2) + ( (y2 - y1) ** 2) )

def closest_centroid(point, centroids):
  # distances_from_centroids is a list containing the distance of point from every centroid
  distances_from_centroids = list(map(lambda centroid : eucledian_dist(point, centroid), centroids))
  # the index of the smallest element in the distances_from_centroids list is then returned, as that would give the cluster number
  # to which point should belong, being closest to the centroid of that cluster
  return distances_from_centroids.index(min(distances_from_centroids))

def assign_points_to_clusters(centroids, points, k):
  clusters = [[] for i in range(k)]
  for point in points :
    clusters[closest_centroid(point, centroids)].append(point)
  return clusters

def calc_centroid_of_cluster(cluster):
  sum_x = 0
  sum_y = 0
  for cluster_point in cluster:
    sum_x += cluster_point[0]
    sum_y += cluster_point[1]
  return [(sum_x/len(cluster)), (sum_y/len(cluster))]

def recompute_centroids(clusters):
  centroids = []
  for cluster in clusters:
    centroids.append(calc_centroid_of_cluster(cluster))
  return centroids

def k_means(k):

  # random.sample(range(0, 99), k) returns k random integers in the range of 0 to 99 (as a list)
  #
  # the map function runs the function in the first parameter over all values in the list in the second parameter
  # and stores all the return values in a map object. What we do here is run the lambda function in the first parameter of map ()
  # over the list of k random integers generated by the second index of map(). In each iteration, index takes a value in the list of 
  # random integers, and returns an array containing the x and y co-ordinate of the indexth point. 
  # 
  # We pass the entire thing to the list() function to convert the map object into a list
  # Ultimately, centroids would contain a list of k lists, each having the x and y co-ordinate of a random point
  # which is initially taken as a centroid 
  #
  # Note : it isn't necessary that the initial three centroids have to be points in the dataset

  centroids = list(map(lambda index: [x[index], y[index]] ,random.sample(range(0, 99), k)))
  
  # clusters would store a list of k lists, with nth list containing all points in the nth cluster
  # initially, clusters is a list containing of k empty lists
  clusters = [[] for i in range(0,k)]

  # We then assign points to their respective clusters based on the centroid of which cluster is closest to the point
  # and then recompute the centroid of each cluster as the centroid of all points in a cluster
  # The more we repeat the above two steps, the more accurate the clustering is, and for this dataset, 100 is more than enough
  # iterations to get accurate clustering based off the k-means algorithm

  for i in range(100):

    # assign_points_to_clusters() returns a list containing k lists, each representing a cluster, 
    # and each of these cluster lists further contains the x,y co-ordinates of all the points in that cluster.
    # The function takes the current list of centroids, points and the value of k, computes for each point which cluster
    # it should be assigned to depending on the distance of the point from the centroid of each cluster, and then accordingly updates 
    # list containing the clusters and the points in each of them, and returns the list after the computation has been done for all points
    #
    # Furthermore, this step is run before the recomputing centroids step because initially we take any three random points as the centroids,
    # after which we first assign the points to clusters taking these three random points to be the centroids in the first iteration

    clusters  =  assign_points_to_clusters(centroids, points, k)

    # the centroids are then recomputed using recompute_centroids(), which takes in the list containing all the clusters
    # and the points contained within them. The function returns the new list of centroids corresponding to each cluster.
    # In the next iteration, this new list of centroids is then used to again assign points to their respective clusters and so on
    
    centroids = recompute_centroids(clusters)

  # print the x co-ordinate of all the points in cluster 0  
  print([point[0] for point in clusters[0]])


x = [] # Store x co-ordinate of each point
y = [] # Store y co-ordinate of each point
points = [] # list containing list of x and y co-ordinates of each point
actual_label = [] # Stores the actual label of each point

with open('dataset.csv', 'r') as dataset_csv_file: # 'r' is read mode
    csv_reader = csv.reader(dataset_csv_file)

    for line in csv_reader:
      # Skip the first line having the column names
      if(line[0] == ''):
        continue
      # line[0] has the serial number of the point, line[1] the x-coordinate, 
      # line[2] the y co-ordinate and line[3] its actual label
      x.append(float(line[1]))
      y.append(float(line[2]))
      points.append([float(line[1]), float(line[2])])
      actual_label.append(line[3])
      #print(line)

# the k means clustering algorithm requires k, that is the number of clusters
# while there are ways to gather the optimum value of k, for now we give it the
# optimum value for the given dataset, which is 3
num_clusters = 3
#print(x)

k_means(num_clusters)









