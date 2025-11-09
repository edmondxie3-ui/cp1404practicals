import datetime

class Project:

    def __init__(self, name="", start_date=datetime, priority=0, cost_estimate=0, completion_percent=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percent}%")

    def __lt__(self,other):
        return self.priority < other.priority
