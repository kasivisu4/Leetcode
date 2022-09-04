class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totalDist = sum(distance)
        if start>destination:
            start,destination = destination,start
        dist = sum(distance[start:destination])
        return min(dist,totalDist-dist)
            