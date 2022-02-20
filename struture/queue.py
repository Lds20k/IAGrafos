class Queue:
    def __init__(self):
        self.queue = []
  
    def push(self, item):
        self.queue.append(item)
  
    def is_empty(self):
        return len(self.queue) == 0
    
    def pop(self):
        if(self.is_empty()):
            return None
        else:
            return self.queue.pop(0)