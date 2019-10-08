from abc import ABC

class Command(ABC):
    def __init__(self, options, argv):
        ...
    
    def exec(self):
        ...