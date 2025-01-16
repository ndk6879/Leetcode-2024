class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def getDistance(a,b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        distances = []
        points = [p1,p2,p3,p4]

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance = getDistance(points[i],points[j])
                distances.append(distance)

        setDistance = set(distances)
        if not len(setDistance) == 2: return False

        line, diagonal = sorted(setDistance)

        
        return distances.count(line) == 4 and distances.count(diagonal) == 2