'''
Write a python program to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using quick sort and display
top five scores.

'''

def quicksort(Percentage,start,end):
    if end-start>1:
        p = partition(Percentage,start,end)
        quicksort(Percentage,start,p)
        quicksort(Percentage,p+1,end)

def partition(Percentage,start,end):
    pivot = Percentage[start]
    i = start+1
    j = end-1

    while True:
        while(i<=j and Percentage[i]<=pivot):
            i = i+1
        while(i<=j and Percentage[j]>=pivot):
            j = j-1

        if i<=j:
            Percentage[i],Percentage[j] = Percentage[j],Percentage[i]
        else:
            Percentage[start],Percentage[j] = Percentage[j],Percentage[start]
            return j


Percentage = []
number = int(input("Enter the Total Number of Students:\n"))
for i in range(number):
    value = float(input("Enter the Percentage:\n "))
    Percentage.append(value)
quicksort(Percentage,0,len(Percentage))
print(Percentage)    




print("The Top five scores are:",Percentage)
minimum = len(Percentage)-6
maximum = len(Percentage)-1
index = 1
for i in range(maximum,minimum,-1):
    if i>=0:
        print(f"{index} Top Scorer:",Percentage[i],"\n")
        index+=1