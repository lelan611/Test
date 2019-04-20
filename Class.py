class Student(object):
    def __init__(self, name, sex, age):
        self._name = name
        self._sex = sex
        self._age = age

    def __getattr__(self, item):
        if item == "isFemale":
            return self._sex == "Female"

Mary = Student("Mary", "Female", 15)
print Mary.isFemale