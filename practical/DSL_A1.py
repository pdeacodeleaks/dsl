'''
In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions) 

'''
def Addelem(A, a):
    for i in range(a):
        elem = input("Enter the name of student:")
        if (elem not in A):
            A.append(elem)
        else:
            while (elem in A):
                print("Duplicate entry")
                elem = input("Enter the name of student:")
            A.append(elem)

def union(AUC, A, C, c):
    AUC.extend(A)
    for i in range(c):
        if (C[i] not in A):
            AUC.append(C[i])

A = []
a = int(input("Enter no. of students playing Cricket: "))
Addelem(A, a)
print("The students Playing Cricket are ", A)
print("\n")

B = []
b = int(input("Enter no. of students playing Badminton: "))
Addelem(B, b)
print("The students Playing Badminton are ", B)
print("\n")

C = []
c = int(input("Enter no. of students playing Football: "))
Addelem(C, c)
print("The students Playing Football are ", C)
print("\n")

U = []
for i in range(a):
    U.append(A[i])
for i in range(b):
    if (B[i] not in U):
        U.append(B[i])
for i in range(c):
    if (C[i] not in U):
        U.append(C[i])
u = len(U)
print("The Universal set is", U)
print("The students Playing Cricket are ", A)
print("The students Playing Badminton are ", B)
print("The students Playing football are ", C)
print("\n")

D = []
for i in range(a):
    if (A[i] in B):
        D.append(A[i])
d = len(D)
print("List of students who play both Cricket and Badminton: ", D)
print("\n")

E = []
for i in range(a):
    if (A[i] not in D):
        E.append(A[i])
for i in range(b):
    if (B[i] not in D):
        E.append(B[i])
e = len(E)
print("List of students who play either cricket or badminton but not both: ", E)
print("\n")

AUB = []
union(AUB, A, B, b)
F = []
for i in range(u):
    if (U[i] not in AUB):
        F.append(U[i])
f = len(F)
print("The No. of student who play neither Cricket nor Badminton is: ", f)
print("The student who play neither Cricket nor Badminton are: ", F)
print("\n")

AUC = []
union(AUC, A, C, c)
auc = len(AUC)

G = []
for i in range(auc):
    if (AUC[i] not in B):
        G.append(AUC[i])
g = len(G)
print("The No. of student who play cricket and Football but not badminton is: ", g)
print("The student who play cricket and Football but not badminton : ", G)
