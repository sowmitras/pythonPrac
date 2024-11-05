class User:
    def __init__(self,id,name,salary,department,number):
        self._id = id
        self._name = name
        self._salary = salary
        self._department = department
        self._number = number
    
    # getter method
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def depart(self):
        return self._department

    @property
    def phone(self):
        return self._number
    
    #setter method
    @name.setter
    def name(self, value: str):
        self._name = value

    @salary.setter
    def salary(self, value: float):
        self._salary = value

    @depart.setter
    def depart(self, value: str):
        self._department = value

    @phone.setter
    def phone(self, value: int):
        self._number = value

    def to_dict(self):
        return { 
            "id": self._id, 
            "name": self._name, 
            "salary": self._salary, 
            "department": self._department, 
            "number": self._number}
    
    def __repr__(self):
        return (f"(id={self._id}, name='{self._name}', "
                f"salary={self._salary}, department='{self._department}', number={self._number})")
