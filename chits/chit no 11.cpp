
/*

 Queues are frequently used in computer programming, 
 and a typical example is the creation of a job queue by an operating system. 
 If the operating system does not use priorities, 
 then the jobs are processed in the order they enter the system. 
 Write C++ program for simulating job queue. 
 Write functions to add job and delete job from queue.


*/

#include<iostream>
using namespace std;

class Node {
public:
    int data; // job no
    char priority;
    Node* next;
    Node *prev;
};

Node* createNode(int data, char priority) {
    Node *t;
    t = new Node(); // dynamically allocate memory
    t->data = data; // Job No;
    t->priority = priority; // priority
    t->next = NULL;
    t->prev = NULL;
    cout << "\n Job Scheduled " << data << " with priority " << priority;
    return(t);
}

int deque(Node **f) {
    if (*f == NULL) {
        cout << "\n QEmpty:\n";
        return(-1);
    }
    Node *t;
    t = *f;
    *f = t->next;
    int t1 = t->data;
    cout << "\ndeleting:" << t1 << "\n";
    delete(t);
    return(t1);
}

Node* enqueue(Node *e, int data, char priority) {
    Node *t, *h;
    t = createNode(data, priority); // allocate memory to node or seat
    h = e;
    h->next = t;
    t->prev = h;
    e = t;
    e->next = NULL; // e->next=head;
    return (e);
}

void printQ(Node *h, int dir) {
    Node *t;
    t = h; // head
    while (t != NULL) {
        cout << "\n Job No:" << t->data << " Priority:" << t->priority;
        if (dir == 1) {
            t = t->next; // forward
        } else {
            t = t->prev; // reverse
        }
    }
}

void display(Node *h1, Node *h2, Node *h3) {
    cout << "\n----Job Execution Sequence ----:";
    printQ(h1, 1); // high priority
    printQ(h2, 1); // medium priority
    printQ(h3, 1); // low priority default
}

int addJob(Node **rearH, Node **rearM, Node **rearL, int data, char priority) {
    switch(priority) {
        case 'H':
            *rearH = enqueue(*rearH, data, priority);
            return(1);
            break;
        case 'M':
            *rearM = enqueue(*rearM, data, priority);
            return(2);
            break;
        case 'L':
            *rearL = enqueue(*rearL, data, priority);
            return(3);
            break;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    char prior[] = {'H', 'L', 'L', 'H', 'M', 'M'};
    Node *frontH, *rearH, *frontM, *rearM, *frontL, *rearL;
    int flag1 = 0, flag2 = 0, flag3 = 0;
    int t;

    for (int i = 0; i < 6; i++) {
        if (prior[i] == 'H') {
            if (flag1 == 0) {
                frontH = createNode(arr[i], prior[i]);
                rearH = frontH;
                flag1++;
                continue;
            }
        }
        if (prior[i] == 'M') {
            if (flag2 == 0) {
                frontM = createNode(arr[i], prior[i]);
                rearM = frontM;
                flag2++;
                continue;
            }
        }
        if (prior[i] == 'L') {
            if (flag3 == 0) {
                frontL = createNode(arr[i], prior[i]);
                rearL = frontL;
                flag3++;
                continue;
            }
        }
        if ((flag1 > 0) || (flag2 > 0) || (flag3 > 0))
            t = addJob(&rearH, &rearM, &rearL, arr[i], prior[i]);
    }

    display(frontH, frontM, frontL);
    t = addJob(&rearH, &rearM, &rearL, 10, 'M');
    display(frontH, frontM, frontL);
    t = deque(&frontH);
    t = deque(&frontH);
    t = deque(&frontH);
    cout << "High:" << t;
    t = deque(&frontM);
    t = deque(&frontM);
    t = deque(&frontM);
    cout << "Mid:" << t;
    t = deque(&frontL);
    t = deque(&frontL);
    t = deque(&frontL);
    t = deque(&frontM);
    display(frontH, frontM, frontL);
    return(0);
}
