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

print("*"*40)
print("/"*10,"BANK ACCOUNT SYSTEM","/"*10)
bal = 0
while True:
    x=input("Enter transaction in format(D/W) : ")
    tran=x.split(" ")
    op=tran[0]
    amt=int(tran[1])
    if op=="D":
      bal+=amt 
      print("Net Balance: ",bal)
    elif op=="W":
      if (amt>bal):
        print("Insufficient Amount")
        print("Net Balance: ",bal)
      else:
        bal-=amt 
        print("Net Balance: ",bal)
    else:
      print("Invalid Choice.")