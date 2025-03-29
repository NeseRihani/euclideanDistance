points = [(1, 2), (4, 6), (7, 8), (2, 1), (9, 5)]


def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum distance
min_distance = min(distances)
print(f"Minimum Euclidean Distance: {min_distance}")