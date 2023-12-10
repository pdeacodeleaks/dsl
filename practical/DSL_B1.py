'''
Write a pythonprogram to store roll numbers of student in array who attended
training program in random order. Write function for searching whether particular
student attended training program or not, using Linear search and Sentinel search.
b) Write a python program to store roll numbers of student array who attended training
program in sorted order. Write function for searching whether particular student
attended training program or not, using Binary search and Fibonacci search

'''

#linear Search
list_att=[30,15,29,25]  #empty list
def addAttendy():
    roll=int(input("\n Enter roll of attendy:"))
    list_att.append(roll)

def display():
    print(list_att)

def LinearSearch(roll):
    fl=0
    cnt=0
    for i in list_att:
        if roll==i :
            print("FOUND at index : ",cnt)
            fl=fl+1           # if roll in list_att
            break
        cnt+=1
    if(fl==0):
        print("NOT FOUND")

def sentinel(roll):
    size=len(list_att)
    last=list_att[size-1]
    list_att[size-1]=roll  #update the last element with roll to search
    k=0
    while(list_att[k]!=roll):
        k+=1
    if(k<(size-1) or last==roll):
        print("Found at index:",k)
    else:
        print("Not Found")
    list_att[size-1]=last
        
def menu():
    print("*"*40)
    print("1. Add attendy\n2. display\n3.Linear Search\n4. Sentinel \n5.Direct")
    
while(1):
    menu()
    ch=int(input("Enter choice:"))
    if(ch==1):
        addAttendy()
    if(ch==2):
        display()
    if(ch==3): #linear Search
        r=int(input("Enter roll no to search:"))
        LinearSearch(r)
    if(ch==4): #sentinel 
        r=int(input("Enter roll no to search:"))
        sentinel(r)
    if(ch==5): #direct
        r=int(input("Enter roll no to search:"))
        if(r in list_att):
            print("Found")
        else:
            print("Not Found")
    if(ch==0):
        exit()
    
