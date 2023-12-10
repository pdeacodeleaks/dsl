'''
Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following: D
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500

'''
#Program A3 DSL
bal=0
#input transaction Log D 300 W 200

while(1):
    trans=input("MENU:\nD 300\nW 300\nE exit\nEnter Tranaction:")
    t=trans.split(" ")

    print(t[0], t[1])
    if(t[0]=='E') or(t[0]=='e'):
        break

    amt=float(t[1])



    if(t[0]=='D'):
        bal=bal+amt
    elif(t[0]=='W')and(bal>=amt):# Widthraw bal> amt to withdraw
        bal=bal-amt
    else:
        print("Insufficient Amount cannot withdraw")
    print("Balance:",bal)
