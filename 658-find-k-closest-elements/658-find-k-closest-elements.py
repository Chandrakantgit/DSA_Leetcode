class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # find by binary search
        #   arr[mid]<=x<arr[mid+1]
        
        if x<=arr[0] : return arr[:k]
        if arr[-1]<=x : return arr[-k:]
        
        def down_a( a, b, x ) :
            if b==len(arr) : return True
            return abs( arr[a]-x ) <= abs( arr[b]-x )
        
        left = 0
        right = len(arr)-1
        while left<right :
            mid = ( left + right ) // 2
            if arr[mid]<=x<arr[mid+1] :
                break
            elif x<arr[mid] :
                right = mid
            else :
                left = mid
                
        count = 0
        a = mid
        b = mid+1
        while count<k :
            if down_a( a, b, x ) :
                a -= 1
            else :
                b += 1
            count += 1
                
        return [ arr[i] for i in range(a+1,b) ]