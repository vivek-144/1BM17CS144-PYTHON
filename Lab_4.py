class university:
    
    def _init_(self):
        self.marks=-1
        self.age=0
        self.stud_id=""
        
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False
    
    def validate_age(self):
        if (self.age>=21):
            return True
        else:
            return False
        
    def check_qualification(self):
        if (self.validate_age() is True and self.validate_marks() is True):
            if self.marks>=65:
                return True
            else:
                return False
        else:
            return False
    
    def setter(self,marks,age,stud_id):
        self.marks=marks
        self.age=age
        self.stud_id=stud_id
        
    def getter(self):
        print("Student ID : ",self.stud_id)
        print("Age : ",self.age)
        print("Marks : ",self.marks)
    


sid = input("Enter the Student ID - ")
a = int(input("Enter the age of the student - "))
m = int(input("Enter the marks obtained by the student - "))
print("\n\n")

stud1 = university()
stud1.setter(m,a,sid)
stud1.getter()
print("\n")

if stud1.check_qualification() is True:
    print(stud1.stud_id," is Qualified!")
else:
    print(stud1.stud_id," is not Qualified")
