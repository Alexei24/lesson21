class Student:
    def __init__(self, name, age, sex, mark, alive):
        self.name = name
        self.age = age
        self.sex = sex
        self.mark = mark
        self.alive = alive

    def __str__(self):
        return f "{self.name}: age = {self.age};"\
                f "sex = {self.sex}"\
                f "mark = {}"
