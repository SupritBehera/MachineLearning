# For reading the dataset.csv file
import csv

x = [] # Store x co-ordinate of each point
y = [] # Store y co-ordinate of each point
actual_label = [] # Stores the actual label of each point

with open('dataset.csv', 'r') as dataset_csv_file: # 'r' is read mode
    csv_reader = csv.reader(dataset_csv_file)

    for line in csv_reader:
      # Skip the first line having the column names
      if(line[0] == ''):
        continue
      # line[0] has the serial number of the point, line[1] the x-coordinate, 
      # line[2] the y co-ordinate and line[3] its actual label
      x.append(line[1])
      y.append(line[2])
      actual_label.append(line[3])
      #print(line)

num_clusters = 3

