/*
Pizza parlor accepting maximum M orders. Orders are served in first come first served
basis. Order once placed cannot be cancelled. Write C++ program to simulate the system
using circular queue using array.
*/


/*****************************Assignment E3: ****************************/
#include<iostream>
using namespace std;
#define SIZE 3
int Queue[SIZE];
int front=-1;
int rear=-1;
int isEmpty()
{
if(front==rear+1)
{ cout<<"\n QEmpty:" ;
return(1);
}
return(0);
}
int Qfull()
{
if((rear+1) % SIZE==front)
{ cout<<"\n QFull:\n" ;
return(1);
}
return(0);
}
void enque(int data)
{
if(!Qfull())
{
if(front==-1)
front=0;
rear++;
Queue[rear]=data;
cout<<"\n Inserted :"<<data<<"\n";
return;
}
cout<<"\n Cannot insert:"<<data<<"\n";
}
int deque()
{
if(!isEmpty())
{
int t=Queue[front];
front++;
cout<<"\nfront:"<<front<<"\n";
return(t);
}
}
int main()
{
enque(10);
enque(20);
enque(30);
enque(40);
cout<<deque()<<"\n";
enque(40);
cout<<deque()<<"\n";
cout<<deque()<<"\n";
cout<<deque()<<"\n";
cout<<deque()<<"\n";
return(0);
}
