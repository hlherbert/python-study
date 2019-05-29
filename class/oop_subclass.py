class SchoolMember:
    """代表任何学校里的成员。"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        """告诉我有关我的细节"""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    """代表一位老师"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    """代表一位学生。"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


class Pig(SchoolMember):
    """代表一头猪。"""

    def tell(self):
        SchoolMember.tell(self)


t = Teacher(name='Mrs. Shrividya', age=40, salary=3000)
s = Student(name='Swaroop', age=25, marks=75)
p = Pig(name='Mr. Pig', age=2)
print()

members = [t, s, p]
for member in members:
    member.tell()
    print(member.__doc__)

print(p.__class__)
