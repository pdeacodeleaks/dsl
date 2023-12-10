/*

Write C++ program for storing binary number using doubly linked lists. Write functions-
To compute 1‘s and 2‘s complement
Add two binary numbers


*/


#include <iostream>
#include <string.h>
using namespace std;

class Node {
public:
    bool bit;
    Node *next_node, *prev_node;

    Node() {
        next_node = NULL;
        prev_node = NULL;
        bit = 0;
    }
};

class List {
private:
    Node *start, *last;

public:
    List() {
        start = NULL;
        last = NULL;
    }

    void input() {
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            Node *temp = new Node();
            if (s[i] == '0') {
                temp->bit = 0;
            } else {
                temp->bit = 1;
            }
            temp->next_node = NULL;
            if (start == NULL) {
                start = temp;
                start->prev_node = NULL;
                last = start;
            } else {
                temp->prev_node = last;
                last->next_node = temp;
                last = last->next_node;
            }
        }
    }

    void one_complement() {
        Node *temp = new Node();
        temp = start;
        while (temp != NULL) {
            if (temp->bit == 1) {
                temp->bit = 0;
            } else {
                temp->bit = 1;
            }
            temp = temp->next_node;
        }
    }

    void two_complement() {
        Node *temp = new Node();
        one_complement();
        temp = last;
        while (temp->bit != 0) {
            temp->bit = 0;
            temp = temp->prev_node;
        }
        temp->bit = 1;
    }

    void print() {
        Node *temp;
        temp = start;
        while (temp != NULL) {
            cout << temp->bit;
            temp = temp->next_node;
        }
    }

    bool add_bit_at_begin(bool x) {
        Node *node = new Node();
        node->bit = x;
        node->next_node = NULL;
        node->prev_node = NULL;
        if (start == NULL) {
            start = node;
        } else {
            node->next_node = start;
            start->prev_node = node;
            start = node;
        }
        return true;
    }

    List operator+(List l1) {
        List sum;
        Node *a = last;
        Node *b = l1.last;
        bool carry = false;
        while (a != NULL && b != NULL) {
            sum.add_bit_at_begin((a->bit) ^ (b->bit) ^ carry);
            carry = ((a->bit && b->bit) || (a->bit && carry) || (b->bit && carry));
            a = a->prev_node;
            b = b->prev_node;
        }
        while (a != NULL) {
            sum.add_bit_at_begin(a->bit ^ carry);
            a = a->prev_node;
        }
        while (b != NULL) {
            sum.add_bit_at_begin(b->bit ^ carry);
            b = b->prev_node;
        }
        if (carry == 1) {
            sum.add_bit_at_begin(carry);
        }
        return sum;
    }
};

int main() {
    List l, l1, l2;
    char u;
    cout << "Enter a binary Number" << endl;
    l.input();
    int c;
    while (u != 'n') {
        cout << "1. One's Complement" << endl;
        cout << "2. Two's Complement" << endl;
        cout << "3. Add 2 binary Numbers" << endl;
        cin >> c;
        if (c == 1) {
            l.one_complement();
            l.print();
            l.one_complement();
        } else if (c == 2) {
            l.two_complement();
            l.print();
            l.two_complement();
        } else if (c == 3) {
            cout << "Enter a binary Number" << endl;
            l1.input();
            l2 = l + l1;
            l2.print();
        }
        cout << endl;
        cout << "Do you want to try again (y/n)" << endl;
        cin >> u;
    }
    return 0;
}
