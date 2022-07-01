class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        l = len(boxTypes)
        
        
        for x in range(l):
            for y in range(l-1):
                if boxTypes[y][1] > boxTypes[y+1][1]:
                    boxTypes[y],boxTypes[y+1] = boxTypes[y+1],boxTypes[y]
        items = 0
        for j in range(l-1,-1,-1):
            if boxTypes[j][0] < truckSize:
                items = items + boxTypes[j][0]*boxTypes[j][1]
                truckSize -= boxTypes[j][0]
            else:
                items = items + truckSize*boxTypes[j][1]
                break
        return items
                
                