import heapq
class PriorityQueue(object):
    def __init__(self):
        self._list = []

    def append(self, element, priority):
        """
        Keep the priority queue always sorted
        """
        heapq.heappush(self._list, (-priority, element))

    def pop(self):
        return heapq.heappop(self._list)[1]