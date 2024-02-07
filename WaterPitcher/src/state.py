class StateClass:
    def __init__(self, pitchers, current, parent, g, h):
        self.pitchers = pitchers
        self.current=current
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.f == other.f

    def __hash__(self):
        return hash(tuple(self.pitchers))


