#Chit 1: In second year computer engineering class, group A student’s play cricket, group B Students play badminton and group C students play football. Write a Python program using functions to compute following: -
#List of students who play both cricket and badminton
#List of students who play either cricket or badminton but not both
#Number of students who play neither cricket nor badminton
#Number of students who play cricket and football but not badminton.
#(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)

def createSet(l1):
    t = set(l1)
    return t

def createGrp(grpName="Noname"):
    members = []
    n = int(input("Enter nos of members in group " + grpName + " :"))
    for i in range(0, n):
        m = input("Enter Member name/id:")
        members.append(m)
    return createSet(members)

def menu(ch):
    if ch == 1:
        return "1.List of students who play both cricket and badminton:"
    elif ch == 2:
        return "2.List of students who play either cricket or badminton but not both:"
    elif ch == 3:
        return "3.Nos of students who play neither cricket nor badminton:"
    elif ch == 4:
        return "4.Nos of students who play cricket and football but not badminton:"
    elif ch == 5:
        return "5.Exit"

def printMenu():
    for i in range(1, 6):
        print(menu(i))
    return

def intersection(s1, s2):
    inter = set([])
    for i in s1:
        if i in s2:
            inter.update(i)
    return inter

def union(s1, s2):
    s3 = intersection(s1, s2)
    for i in s1:
        if i not in s3:
            s3.update(i)
    for i in s2:
        if i not in s3:
            s3.update(i)
    return s3

def difference(s1, s2):
    diff = s1
    for i in s2:
        if i in s1:
            diff.remove(i)
    return diff

cricket = createGrp("Cricket")
badminton = createGrp("Badminton")
football = createGrp("Football")

print("-" * 50, "\nCricket Players:", cricket)
print("Batminton Players:", badminton)
print("Football Players:", football)

while True:
    print("-" * 23, "Menu", "-" * 21)
    printMenu()
    print("=" * 50)
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        break
    elif ch == 1:
        q1 = intersection(cricket, badminton)
        print(menu(1))
        print(q1)
    elif ch == 2:
        q1 = union(cricket, badminton)
        print("union:", q1)
        q2 = intersection(cricket, badminton)
        print("intersection:", q2)
        print(menu(2))
        print(difference(q1, q2))
    elif ch == 3:
        q1 = union(cricket, badminton)
        q2 = difference(football, q1)
        print(menu(3))
        print(len(q2), "==>", q2)  # symmetric_difference
    elif ch == 4:
        q1 = intersection(cricket, football)
        q2 = difference(q1, badminton)
        print(menu(4))
        print(len(q2), "==>", q2)
    else:
        print("invalid choice:")
