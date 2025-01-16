import uuid
import re
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
    
    def get_all(self):
        with open("todo.txt") as f:
            for line in f:
                if not line:
                    break
                print(line)
                
    def get_by_id(self,id)
        with open("todo.txt") as f:
            for line in f:
                if not line:
                    break
                info = re.split(r',',line)
                if info[0] == id:
                    print(line)
    def update_by_id(self):
        line_to_update = 1
        found = False
        with open("todo.txt") as f:
            for line in f:
                if not line:
                    break
                info = re.split(r',',line)
                if info[0] == self.id:
                    found = True
                    break
                line_to_update +=1
        if not found:
            print("to do not found")
            return
        with open("todo.txt") as f:
            lines = f.readlines()

        if 0<line_to_update<len(lines):
            lines[line_to_update-1] = f"{id}, {self.title}, {self.description}, {self.due_date}, {self.status}"
        with open("todo.txt",mode="w") as f:
            f.write(lines)

    def delete_by_id(self):
        line_to_delete = 1
        found = False
        with open("todo.txt") as f:
            for line in f:
                if not line:
                    break
                info = re.split(r',',line)
                if info[0] == self.id:
                    found = True
                    break
                line_to_delete +=1
        if not found:
            print("to do not found")
            return
        with open("todo.txt") as f:
            lines = f.readlines()

        if 0<line_to_delete < len(lines):
            del lines[line_to_delete-1]

        with open("todo.txt", mode="w") as f:
            f.write(lines)
