# Sahaana Iyer         8609            Batch B          TE Computers
import random
import math
def npoints (n) :
    points = []
    i=0
    while (i<n) : 
        print("Enter x co-ordinate of point ", i+1, " - ")
        a = int(input())
        print("Enter y co-ordinate of point ", i+1, " - ")
        b = int(input())
        if (a,b) not in points :
            points.append((a,b))
        else :
            print("Point already entered; Please enter another point")
            i=i-1
        i=i+1
    return points
def kpoints (k) :
    kpoints = []
    i=0
    while (i<k) : 
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        if (a,b) not in kpoints :
            kpoints.append((a,b))
        else :
            i=i-1
        i=i+1
    return kpoints

def euclid_dist(a1, a2, b1, b2) :
    dist = math.sqrt((b1-a1)**2 + (b2-a2)**2)
    return dist

def assign_cluster(points, kpoints) :
    point_cluster_center = []
    for a1, a2 in points :
        dist = []
        for b1, b2 in kpoints :
            d = euclid_dist(a1, a2, b1, b2)
            dist.append(d)
        min_index = dist.index(min(dist))
        point_cluster_center.append(kpoints[min_index])
    point_cluster_center_index = []
    for i in point_cluster_center :
        for j in kpoints :
            if i==j :
                ind = kpoints.index(i)
                point_cluster_center_index.append(ind)
    return point_cluster_center_index

def update_cluster(points, kpoints, point_cluster_center_index) :
    for i in range(len(kpoints)) :
        mean = []
        for j in points :
            if i==point_cluster_center_index[points.index(j)] :
                mean.append(j)
        print("Mean : ", mean)
        meana = kpoints[i][0]
        meanb = kpoints[i][1]
        meanlen = len(mean)+1
        if meanlen != 0 :
            for a, b in mean :
                meana = meana + a 
                meanb = meanb + b
            kpoints[i] = (meana//meanlen, meanb//meanlen)
    return kpoints

n = int(input("Enter number of points : "))
points = npoints(n)
print("The points are ", points)
k = int(input("Enter number of clusters : "))
kpoints = kpoints(k)
print("The cluster centers are ", kpoints)
point_cluster_center_index = assign_cluster(points, kpoints)
print("The points belong to clusters ", point_cluster_center_index)
prev_kpoints = []
point_cluster_center_index_prev = []
iter = 1
while ((iter <= 10) and prev_kpoints!=kpoints and point_cluster_center_index!=point_cluster_center_index_prev) :
    print("\nIteration Number ", iter, " :-")
    point_cluster_center_index_prev = point_cluster_center_index
    prev_kpoints = kpoints.copy()
    kpoints = update_cluster(points, kpoints, point_cluster_center_index)
    point_cluster_center_index = assign_cluster(points, kpoints)
    print("The points belong to clusters ", point_cluster_center_index)
    print("The new cluster centers are ", kpoints)
    iter = iter + 1