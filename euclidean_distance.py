import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 9), (8, 3), (2, 1)]  # Örnek noktalar, kendi noktalarınızı buraya ekleyin

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
