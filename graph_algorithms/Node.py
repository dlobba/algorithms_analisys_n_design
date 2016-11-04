class Node:
    def __init__ (self, value, adjacent = None):
        self.value = value
        if adjacent == None:
            self.adjacent = list ()
        else:
            self.adjacent = list (adjacent)
        self.color = None
        self.distance = float('inf')
        self.parent = None
        
    def __repr__ (self):
        out = self.value + " /d=" + str (self.distance) +\
              " /c=" + str(self.color) + " /adj={"
        
        if len (self.adjacent) != 0:
            out += self.adjacent[0]
            for next in self.adjacent[1:]:
                out += "->" + next
        out += "}"
        return out
        
    
    def __str__ (self):
        return self.value
