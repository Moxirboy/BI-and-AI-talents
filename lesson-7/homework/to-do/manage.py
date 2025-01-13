import uuid
class to_do:
    def __init__(self,id=None,title=None, description=None, due_date=None,status=None):
        self.id = id  if id is not None else uuid.uuid4() 
        self.title = title  if title is not None else None
        self.description = description  if description is not None else None
        self.due_date = due_date  if due_date is not None else None
        self.status = status  if status is not None else None
    
    def create(self):
        with open("to-do.txt") as f:
            f.write(f"{self.id}, {self.title}, {self.description}, {self.due_date}, {self.status}")
        