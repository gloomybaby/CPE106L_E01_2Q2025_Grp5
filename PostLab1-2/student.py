import random
"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Returns if equal"""
        if (self.name == other.name):
            return "Equal"
        else:
            return "Not Equal"

    def __lt__(self, other):
        """Returns if less than"""
        if (self.name < other.name):
            return "Less Than"
        else:
            return "Not Less Than"

    def __gt__(self, other):
        """Returns if greater than"""
        if (self.name > other.name):
            return "Greater Than"
        elif (self,name == other.name):
            return "Both are Equal"
        else:
            return "Not Greater Than or Equal"

def main():
    """A simple test."""
    studentList = []

    student1 = Student("Ken", 5)
    print(student1)
    for i in range(1, 6):
        student1.setScore(i, 100)
    studentList.append(student1)

    student2 = Student("Barbie", 5)
    print(student2)
    for i in range(1, 6):
        student2.setScore(i, 100)
    studentList.append(student2)

    student3 = Student("Juan", 5)
    print(student3)
    for i in range(1, 6):
        student2.setScore(i, 100)
    studentList.append(student3)

    random.shuffle(studentList)

    print("\nUnsorted List of Students: \n")
    for i in studentList:
        print(i.__str__())
    
    print("\nSorted List of Students: \n")
    studentList.sort(key = lambda x:x.name)

    for i in studentList:
        print(i.__str__())

    print("\nComparison\n")
    print(student1==student2)
    print(student1<student2)
    print(student2<student1)
    print(student1>student2)

if __name__ == "__main__":
    main()
