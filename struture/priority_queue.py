import heapq


class PriorityQueue:
  def __init__(self):
    self.queue = []
  
  def push(self, item):
    heapq.heappush(self.queue, item)
  
  def pop(self):
    if(self.is_empty()):
        return None
    else:
        return heapq.heappop(self.queue)

  def is_empty(self):
    return len(self.queue) == 0