from functools import cmp_to_key
from PIL import Image, ImageDraw

# A class used to store the x and y coordinates of points
class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

# A global point needed for sorting points with reference
# to the first point
p0 = Point(0, 0)

# A utility function to find next to top in a stack
def nextToTop(S):
    return S[-2]

# A utility function to return square of distance
# between p1 and p2
def distSq(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +
            (p1.y - p2.y) * (p1.y - p2.y))


# To find orientation of ordered triplet (p, q, r).
def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) -
           (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clock wise
    else:
        return 2  # counterclock wise


# A function used by cmp_to_key function to sort an array of
# points with respect to the first point
def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if distSq(p0, p2) >= distSq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1


# Convex hull of a set of n points.
def convexHull(points, n):
    ymin = points[0].y
    min = 0
    for i in range(1, n):
        y = points[i].y
        if ((y < ymin) or
                (ymin == y and points[i].x < points[min].x)):
            ymin = points[i].y
            min = i

    points[0], points[min] = points[min], points[0]
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))
    m = 1
    for i in range(1, n):
        while ((i < n - 1) and
               (orientation(p0, points[i], points[i + 1]) == 0)):
            i += 1

        points[m] = points[i]
        m += 1
    if m < 3:
        return
    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])
    for i in range(3, m):
        while ((len(S) > 1) and
               (orientation(nextToTop(S), S[-1], points[i]) != 2)):
            S.pop()
        S.append(points[i])
    xy =[]
    while S:
        p = S[-1]
        xy.append(p.x)
        xy.append(540-p.y)
        S.pop()
    f = open('DS2.txt', 'r')
    data = f.readlines()
    input_points = []
    for line in data:
        k, j = line.split(" ")
        input_points.append(int(j))
        input_points.append(540 - int(k))
    f.close()

    canvas = Image.new("RGB", (960, 540), (255, 255, 255))
    d = ImageDraw.Draw(canvas)
    d.point(xy, fill=(255, 0, 0))
    d.point(input_points, fill=0)
    d.line(xy, fill=(0, 0, 255), width=1)
    canvas.show()
    canvas.save("pictureHull.png")

# Driver Code
f = open('DS2.txt', 'r')
data = f.readlines()
f.close()
points = []
for i in range(0, len(data)):
    data[i] = data[i].split()
    points.append(Point(int(data[i][1]), int(data[i][0])))

n = len(points)
convexHull(points, n)



