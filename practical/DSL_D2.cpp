/*
In any language program mostly syntax error occurs due to unbalancing delimiter such as
(),{},[]. Write C++ program using stack to check whether given expression is well
parenthesized or not.

*/

#include<iostream>
#include <string>
using namespace std;
#define SIZE 100
int stack[SIZE];
int top=-1;
int stackFull()
{
if(top==SIZE-1)
return(1);
return(0);
}
int stackEmpty(){
if(top==-1)
return(1);
return(0);
}
void push(int data)
{
cout<<"\npushing.."<<char(data)<<"\n";
if(!stackFull())
{
top++;
stack[top]=data;
return;
}
cout<<"Stack Full";
}
int pop()
{
if(!stackEmpty())
{
char data=stack[top];
cout<<"\nPoping: "<<char(data)<<"\n";
top--;
    return(data);
}
cout<<"Stack Empty";
return(' ');
}
int analyser(string s1,string open,string close)
{
int len=s1.length();
int i=0;
cout<<"\nanalysing...";
//return 0;
while(len>=0)
{
int ch=int(s1[i]);
if((ch==int(open[0]))||(ch==int(open[1]))||(ch==int(open[2])))
{
push(ch);
}
else if((ch==int(close[0]))||(ch==int(close[1]))||(ch==int(close[2])))
{
if(stackEmpty()) //Check if error
return(1);
int t=pop();
switch(ch)
{
case 125: //}
   //cout<<"searching for block { Found }";
if(t!=123) //{ {
{
cout<<"\nSyntax Error misplaced :"<<char(123);
return(1);
}
break;
case 41: //)     
//cout<<"searching for symbol ( found )";
if(t!=40) //(
{cout<<"\nSyntax Error misplaced "<<char(40);
return(1);
}
break;
case 93: //]
//cout<<"searching for symbol [ found ]";
if(t!=91) //[
{cout<<"\nSyntax Error misplaced "<<char(91);
return(1);
}

break;
default:
break;
}
}
len--;
i++;
}
if(!stackEmpty())
return(1);
return(0);
}
int main()
{
string s1="{int arr [10];\nint a=10,b=20;\nif((a>b)&&(a>0)&&(b>0))\n{cout<<\"a is greater\";\n}\nelse{\ncout<<\"b is greater\";\n}}";
s1="((a+b)/(c-d))";
string open="{(["; //ASCII 123 40 91 {   (   [
string close="})]"; //ASCII 125 41 93 } ) ]
//cout<<int(close[2]);
cout<<"\nOriginal Code\n"<<s1;
int res=analyser(s1,open,close);
if(res==1)
cout<<"\nError: Delimiters are not Balanced";
else
cout<<"\nDelimiters are Balanced";
return 0;
}
