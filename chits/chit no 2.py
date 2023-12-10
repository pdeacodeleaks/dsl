#Chit 2: Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
#The average score of class
#Highest score and lowest score of class
#Count of students who were absent for the test
#Display mark with highest frequency
# Program A2 DSL
#Write a Python program to store marks scored in subject “Fundamental of Data
#Structure” by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

class student:
    subject = "Fundamental of Data Structure"
    max_marks = 100
    
    def __init__(self, marks=0):
        print("Student created for subject is ", student.subject)
        self.marks = marks
        
    def setmarks(self, marks):
        self.marks = marks
    
    def getmarks(self):
        return self.marks


menu1 = ["1.Add Student to class:", "2.The average score of class:", "3.Highest score and lowest score of class:",
         "4.Count of students who were absent for the test:", "5.Display mark with highest frequency:", "6.Exit"]


def printMenu():
    print("-" * 20, "MENU", "-" * 20)
    for i in range(0, len(menu1)):
        print(menu1[i])
    print("-" * 50)
    return


score = []
while True:
    printMenu()
    ch = int(input("Enter ur choice:"))
    if ch == 6:
        break
    elif ch == 1:
        print(menu1[0])
        marks = int(input("Enter Students marks -1 if Absent max marks:" + str(student.max_marks) + " subject: " + student.subject))
        if marks > student.max_marks:
            print("Invalid marks")
        s1 = student(marks)
        score.append(s1.getmarks())
        print("Score:", score)
    elif ch == 2:
        print(menu1[1])
        print("Average score of class:", sum(score) / len(score))
    elif ch == 3:
        print(menu1[2])
        print("Highest Score:", max(score))
        sc1 = score.copy()
        sc1.remove(-1)
        print("Lowest Score:", min(sc1))
    elif ch == 4:
        print(menu1[3])
        print("Nos of Student who are absent", score.count(-1))
    elif ch == 5:
        print(menu1[4])
        d = {}
        sc1 = score.copy()
        sc1.remove(-1)
        for i in sc1:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        maxfreq = max(d.values())
        for i in d.keys():
            if d[i] == maxfreq:
                print("MAximum freq marks are:", i, " and freq=", maxfreq)
