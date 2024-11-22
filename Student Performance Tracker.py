class Student:
    
    def __init__(self,name: str, scores: list[int]):
        self.name= name
        self.scores=scores
        print( f"{self.name} is student name and  {self.scores} is scores")
        
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self):
        for score in self.scores:
            if score<40:
                return "Fail"
        return "Pass"        
    
class PerformanceTracker:
    
    def __init__(self):
        self.students={}
    
    def add_student(self,student: Student):
        self.students[student.name]=student
     
    def calculate_class_average(self):
        average=0
        for key in self.students.keys():
            student= self.students[key]
            average+=student.calculate_average()
        print (f"Class average is {average}.")
    
    def display_student_performance(self):
        for key in self.students.keys():
            student= self.students[key]
            print (f"{student.name} average score is {student.calculate_average()} and declared  {student.is_passing()}.")
 
tracker= PerformanceTracker()    
while True:
    try:
        name = input("Enter student name: ")
        if not name.strip():
            print("Student name is empty ")
            continue
        math = int(input("Enter math grade: "))
        science = int(input("Enter science grade: "))
        english = int(input("Enter English grade: "))
        student= Student(name,[math,science,english])       
        tracker.add_student(student)
        user_input= input("Want to enter more student? y / n ")
        if user_input.lower()=="n":
            break
        else:
            continue
    except ValueError:
        print("Try again by providing a valid value.")

tracker.display_student_performance()
tracker.calculate_class_average()