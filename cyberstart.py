points = [(1,4),(3,5),(4,6),(7,2)]
import math
def euclideanDistance(point1,point2):
    x1,y1 =point1
    x2,y2 =point2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

distances = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
                   distance = euclideanDistance(points[i],points[j])
                   distances.append(distance)
min_distance = min(distances)
print("En küçük mesafe: ",min_distance)
