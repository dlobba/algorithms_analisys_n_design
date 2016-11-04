class Queue:
    def __init__ (self):
        self.items = list ()
    
    def isEmpty (self):
        if len (self.items) == 0:
            return True
        else:
            return False
    
    def enqueue (self, item):
        self.items.insert (0, item)
    
    def dequeue (self):
        return self.items.pop ()
    
    def __repr__ (self):
        out = "["
        for item in self.items:
            out += str(item)
        out += "]"
        return out
    
    def __str__ (self):
        return repr(self)
        
