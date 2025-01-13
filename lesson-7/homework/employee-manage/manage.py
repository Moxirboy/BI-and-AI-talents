import uuid
import re
    
class employee:
    def __init__(self, id=None, name=None, position=None, salary=None):
        self.id = id  if id is not None else "asdasd"
        self.name = name if name is not None else "Unknown"
        self.position = position if position is not None else "Unknown"
        self.salary = salary if salary is not None else 0


    def create(self):
        id = uuid.uuid4()
        with open('employee.txt', mode='a') as f:
            f.write(f"{id},{self.name},{self.position},{self.salary}\n")

    def get_by_id(self):
        with open('employee.txt',mode='r') as f:
            while True:
                txt = f.readline()
                if not txt:
                    break
                info = re.split(r',',txt)
                if info[0] == self.id:
                    print(info[1])

    def get_all(self):
        infos = []
        with open('employee.txt', mode='r') as f:
            for line in f:
                if line.strip():
                    info = re.split(r',',line)
                    infos.append(info)
        return infos

    def update_by_id(self):
        line_to_update =1
        with open('employee.txt',mode ='r') as f:
            for line in f:
                if line.strip():
                    info = re.split(r',', line)
                    if self.id in info[0]:
                        break
                    line_to_update +=1
                else:
                    print("no user found")
                    return 
        with open('employee.txt',mode='r') as f:
            lines = f.readlines()

        if 0<line_to_update<=len(lines):
            lines[line_to_update-1] = f"{self.id},{self.name},{self.position},{self.salary}\n"

        with open('employee.txt', mode='w') as f:
            f.write(lines)


    def delete_by_id(self):
        line_number = 1
        with open('employee.txt',mode='r') as f:
            for line in f:
                if line.strip():
                    info = re.split(r',',line)
                    if info[0] == self.id:
                        break
                    line_number +=1
                else:
                    print("no data found")
        with open('employee.txt', 'r') as f:
            lines = f.readlines()

        if 0 < line_number <=len(lines):
            del lines[line_number - 1]

        with open('employee.txt', 'w') as f:
            f.writelinese(lines)