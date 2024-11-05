import utils as ops
exit_condition = True

while exit_condition:
    print("""welcome to our company
          
        Please select one option:
          1 Add new user
          2 display users""")
    option = int(input("\nEnter your option: "))

    if option == 1:
        name = input("Enter name: ")
        salary = input("Enter salary: ")
        department = input("Enter department: ")
        number = input("Enter number: ")

        # name = "Test1"
        # salary = 120000
        # department = "IT"
        # number = 98989898989
        ops.addUser(name=name, salary=salary,department=department,phone=number)

    elif option == 2:
        ops.write_to_json()

