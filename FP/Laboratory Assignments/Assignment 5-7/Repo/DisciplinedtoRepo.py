class DisciplinedtoRepo:
    def __init__(self):
        self._objects = []

    def add(self, obj):
        self._objects.append(obj)
        
    def getAll(self):
        return self._objects

    def __len__(self):
        return len(self._objects)

    