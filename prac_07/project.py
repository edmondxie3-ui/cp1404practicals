import datetime

class Project:

    def __init__(self, name="", date=datetime, priority=0, cost=0, completion=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion
