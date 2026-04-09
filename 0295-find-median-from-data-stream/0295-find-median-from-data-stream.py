import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max heap (store negative values)
        self.large = []  # min heap

    def addNum(self, num):
        # Add to max heap
        heapq.heappush(self.small, -num)

        # Move largest from small → large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance heaps
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0