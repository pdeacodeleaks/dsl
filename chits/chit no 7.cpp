/*
 Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of second, third and final year of department can be granted membership on request. Similarly one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write C++ program to maintain club member‘s information using singly linked list. Store student PRN and Name. Write functions to:
Add and delete the members as well as president or even secretary.
Compute total number of members of club
Display members
Two linked lists exists for two divisions. Concatenate two lists.

*/

#include <iostream>
#include <string>

using namespace std;

struct Node {
    string PRN;
    string name;
    Node* next;

    Node(string prn, string n) : PRN(prn), name(n), next(nullptr) {}
};

class PinnacleClub {
private:
    Node* president;
    Node* secretary;

public:
    PinnacleClub() : president(nullptr), secretary(nullptr) {}

    void addMember(string prn, string name) {
        Node* newNode = new Node(prn, name);

        if (president == nullptr) {
            president = newNode;
            secretary = newNode;
        } else {
            secretary->next = newNode;
            secretary = newNode;
        }
    }

    void deleteMember(string prn) {
        Node* current = president;
        Node* prev = nullptr;

        while (current != nullptr) {
            if (current->PRN == prn) {
                if (prev == nullptr) {
                    president = current->next;
                } else {
                    prev->next = current->next;
                }
                delete current;
                return;
            }
            prev = current;
            current = current->next;
        }

        cout << "Member with PRN " << prn << " not found." << endl;
    }

    void displayMembers() {
        Node* current = president;

        cout << "Club Members:" << endl;
        while (current != nullptr) {
            cout << "PRN: " << current->PRN << ", Name: " << current->name << endl;
            current = current->next;
        }
    }

    int totalMembers() {
        int count = 0;
        Node* current = president;

        while (current != nullptr) {
            count++;
            current = current->next;
        }

        return count;
    }

    void concatenateLists(PinnacleClub& otherClub) {
        if (president == nullptr) {
            president = otherClub.president;
            secretary = otherClub.secretary;
        } else if (otherClub.president != nullptr) {
            secretary->next = otherClub.president;
            secretary = otherClub.secretary;
        }
    }
};

int main() {
    PinnacleClub division1, division2;

    division1.addMember("PRN1", "John");
    division1.addMember("PRN2", "Alice");

    division2.addMember("PRN3", "Bob");
    division2.addMember("PRN4", "Eva");

    division1.displayMembers();
    division2.displayMembers();

    division1.concatenateLists(division2);

    cout << "Concatenated List:" << endl;
    division1.displayMembers();

    return 0;
}