
# Branigan McPeters
# 00083473
# CS 472 ASG 4 Part 1
# 02/25/2023

import pandas as pd
import math
    
# --------------------------------------------------------------------------------------------------------------- #
 
def getTuples(datafile):
    """
    Description: Function reads a csv file with data delimited by commas and creates a list of tuples
    Parameters: A csv file from which to read data
    Return: A list of tuples
    """

    df = pd.read_csv(datafile, header=None)
    lst = df.values.tolist()
    tuple_list = [tuple(x) for x in lst]
    return tuple_list
    
# --------------------------------------------------------------------------------------------------------------- #

def get_distance(x, y, z):
    """
    Description: Function calculates the distance from point z from the line segment connecting point x to point y
    Parameters: Tuples x, y, and z representing xy-coordinates 
    Return: The distance from z to the line between x and y
    """

    distance = (x[0] * y[1] + y[0] * z[1] + z[0] * x[1]) - (x[1] * y[0] + y[1] * z[0] + z[1] * x[0])
    return distance
    
# --------------------------------------------------------------------------------------------------------------- #

def convex_hull_bf(points):
    """
    Description: Function uses brute force to compare every combination of points to find if the point
    is part of the convex hull
    Parameters: a list of points
    Return: A set of points that make up the convex hull
    """

    points = sorted(points)
    size = len(points)
    convex_hull = set()

    for point_x in range(size-1):
        for point_y in range(point_x + 1, size):
            points_left_of_xy = points_right_of_xy = False
            xy_part_of_convex_hull = True
            for point_z in range(size):
                if point_z != point_x and point_z != point_y:
                    position_of_c= get_distance(points[point_x], points[point_y], points[point_z])
                    if position_of_c > 0:
                            points_left_of_xy = True
                    elif position_of_c < 0:
                        points_right_of_xy = True
                    else:
                        # point[i], point[j], point[k] all lie on a straight line
                        # if point[k] is to the left of point[i] or it's to the
                        # right of point[j], then point[i], point[j] cannot be
                        # part of the convex hull of A
                        if points[point_z] < points[point_x] or points[point_z] > points[point_y]:
                            xy_part_of_convex_hull = False
                            break

                if points_left_of_xy and points_right_of_xy:
                    xy_part_of_convex_hull = False
                    break

            if xy_part_of_convex_hull:
                convex_hull.update([points[point_x], points[point_y]])
    convex_hull = sorted(convex_hull)
    print(convex_hull)

# --------------------------------------------------------------------------------------------------------------- #

def construct_hull(current_hull, left_points, right_points, convex_hull):
    """
    Description: Function 
    Parameters: 
    Return: 
    """

    if current_hull:
        extreme_point = None
        extreme_point_distance = -math.inf
        possible_hull_points = []

        for point in current_hull:
            position = get_distance(left_points, right_points, point)

            if position > 0:
                possible_hull_points.append(point)

                if position > extreme_point_distance:
                    extreme_point_distance = position
                    extreme_point = point

        if extreme_point:
            construct_hull(possible_hull_points, left_points, extreme_point, convex_hull)
            convex_hull.add(extreme_point)
            construct_hull(possible_hull_points, extreme_point, right_points, convex_hull)
    
# --------------------------------------------------------------------------------------------------------------- #

def convex_hull_dc(points):
    """
    Description: Function uses decrease and conquer to compare every combination of points to find if the point
    is part of the convex hull
    Parameters: a list of points
    Return: A set of points that make up the convex hull
    """
    points = sorted(points)
    size = len(points)

    far_left = points[0]
    far_right = points[size-1]

    convex_hull = {far_left, far_right}
    upper_hull = []
    lower_hull = []

    for i in range(1, size - 1):
        position = get_distance(far_left, far_right, points[i])

        if position > 0:
            upper_hull.append(points[i])
        elif position < 0:
            lower_hull.append(points[i])
            
    construct_hull(upper_hull, far_left, far_right, convex_hull)
    construct_hull(lower_hull, far_right, far_left, convex_hull)

    convex_hull = sorted(convex_hull)
    print(convex_hull)
    
# --------------------------------------------------------------------------------------------------------------- #

# Driver Function
def main():

  list_of_points = getTuples("test.csv")

  # Brute Force Algorithm
  convex_hull_bf(list_of_points)

  # Decrease and Conquer Algorithm
  convex_hull_dc(list_of_points)

# Call Main
if __name__ == "__main__":
    main()