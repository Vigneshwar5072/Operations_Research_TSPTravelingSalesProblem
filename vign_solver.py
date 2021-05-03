#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import csv
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')
    #print(lines)

    nodeCount = int(lines[0])
    x1 = []

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        #print(parts)
        points.append(float(parts[0]))
        
        res = [(float(parts[0]), float(parts[1])) for i in parts]
        x1.append(list(set(res)))
   
        #print(x1)
        #print(points)

    # build a trivial solution
    # visit the nodes in the order they appear in the file
 
    flattened = [val for sublist in x1 for val in sublist]  
    #print(flattened)
    solution = range(0, nodeCount)


    from scipy.spatial import distance

    Distance_matrix = distance.cdist(flattened, flattened, 'euclidean')
    
    
    item_length = len(Distance_matrix[0])

    with open('ur test.csv', 'w') as test_file:
        file_writer = csv.writer(test_file)
        for i in range(item_length):
            file_writer.writerow([x[i] for x in Distance_matrix])
    
    # calculate the length of the tour
# =============================================================================
#     obj = length(points[solution[-1]], points[solution[0]])
#     print(obj)
#     for index in range(0, nodeCount-1):
#         obj += length(points[solution[index]], points[solution[index+1]])
#         print(obj)
# 
# =============================================================================
    # prepare the solution in the specified output format
    #output_data = '%.2f' % obj + ' ' + str(0) + '\n'
    #output_data += ' '.join(map(str, solution))

    #return output_data


#import sys
# =============================================================================
# 
# if __name__ == '__main__':
#     import sys
#     if len(sys.argv) > 1:
#         file_location = sys.argv[1].strip()
#         with open(file_location, 'r') as input_data_file:
#             input_data = input_data_file.read()
#         print(solve_it(input_data))
#     else:
#         print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')
# =============================================================================

if __name__ == '__main__':
    import sys
    #if len(sys.argv) > 1:
    #   file_location = sys.argv[1].strip()
    file_location = 'C:/Users/per35/Downloads/tsp/data/tsp_5_1'
    with open(file_location, 'r') as input_data_file:
        #print(input_data_file)
        input_data = input_data_file.read()
        print(solve_it(input_data))
    #else:
    #    print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')