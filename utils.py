import json
import user as userDetails

members = []
departments = {}

def addUser(name,salary,department,phone):
    newUserId = len(members)+1
    phBool = False
    newDepartKey = 100
    for user in members:
        if user._number == phone:
            phBool = True

    for k, v in departments.items():
        if v == department:
            newDepartKey = k
        else:
            newDepartKey = len(departments) + 100

    createDepartment(newDepartKey, department)
    
    if phBool:
        print("\nPhone number is Exists. Please enter another phone number")
    else:
        updateUser(userDetails.User(name=name, salary=salary, department=newDepartKey, number=phone, id=newUserId))
        print("\nUser added succcessfully")
    
    
def updateUser(user: userDetails.User):
    members.append(user)
    # write_to_json()

def createDepartment(deptKey, deptValue):
    departments[deptKey] = deptValue

def display_users():
    for user in members:
        print(user)

def write_to_json():
    user_dicts = [user.to_dict() for user in members] 
    output = { "member": user_dicts, "department": departments} 
    json_data = json.dumps(output, indent=4) 
    with open("cms.json", 'w') as file:
      file.write(json_data)
      file.close()

def read_json():
    with open("cms.json", "r") as json_file:
      data = json.load(json_file)

