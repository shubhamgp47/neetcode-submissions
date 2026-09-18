class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        res=[]
        for x,y in points:
            dist=-(x*x+y*y)
            #heapq.heappush(maxHeap, (dist, x, y))
            maxHeap.append([dist,x,y])
            heapq.heapify(maxHeap)
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res

        '''res=[]
        heap=[]
        for x,y in points:
            distance= x*x + y*y
            heap.append([-distance,x,y])
            heapq.heapify(heap)
            if len(heap)>k:
                heapq.heappop(heap)
            while heap:
                dist,x,y=heapq.heappop(heap)
                res.append([x,y])
        return res'''
        


