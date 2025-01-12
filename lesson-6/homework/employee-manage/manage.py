import uuid
import re
def create(name,position,salary):
    id = uuid.uuid4()
    print(id)
    with open('employee.txt', mode='a') as f:
        f.write(f"{id},{name},{position},{salary}\n")

def get_by_id(id):
    with open('employee.txt',mode='r') as f:
        while True:
            txt = f.readline()
            if not txt:
                break
            info = re.split(r',',txt)
            if info[0] == id:
                print(info[1])
        
def get_all():
    infos = []
    with open('employee.txt', mode='r') as f:
        for line in f:
            if line.strip():
                info = re.split(r',',line)
                infos.append(info)
    return infos

def update_by_id(id,name,position,salary):
    line_to_update =1
    with open('employee.txt',mode ='r') as f:
        for line in f:
            if line.strip():
                info = re.split(r',', line)
                if id in info[0]:
                    break
                line_to_update +=1
            else:
                print("no user found")
                return 
    with open('employee.txt',mode='r') as f:
        lines = f.readlines()

    if 0<line_to_update<=len(lines):
        lines[line_to_update-1] = f"{id},{name},{position},{salary}\n"
    
    with open('employee.txt', mode='w') as f:
        f.write(lines)


def delete_by_id(id):
    line_number = 1
    with open('employee.txt',mode='r') as f:
        for line in f:
            if line.strip():
                info = re.split(r',',line)
                if info[0] == id:
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