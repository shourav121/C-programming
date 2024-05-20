#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void displayMenu() {
    cout << "===== Word Editor Menu =====" << endl;
    cout << "1. Create a new document" << endl;
    cout << "2. Open an existing document" << endl;
    cout << "3. Edit document" << endl;
    cout << "4. Save the document" << endl;
    cout << "5. Exit" << endl;
    cout << "============================" << endl;
}

void createDocument() {
    string content;
    cout << "Enter the content of the document. Enter 'EOF' on a new line to finish." << endl;
    string line;
    while (getline(cin, line) && line != "EOF") {
        content += line + "\n";
    }
    ofstream outfile("document.txt");
    outfile << content;
    cout << "Document created successfully." << endl;
}

void openDocument(string& content) {
    ifstream infile("document.txt");
    if (!infile) {
        cerr << "Error opening document!" << endl;
        return;
    }
    content = "";
    string line;
    while (getline(infile, line)) {
        content += line + "\n";
    }
    cout << "Document opened successfully." << endl;
    infile.close();
}

void editDocument(string& content) {
    cout << "Enter new content of the document. Enter 'EOF' on a new line to finish." << endl;
    string line;
    while (getline(cin, line) && line != "EOF") {
        content += line + "\n";
    }
}

void saveDocument(const string& content) {
    ofstream outfile("document.txt");
    outfile << content;
    cout << "Document saved successfully." << endl;
}

int main() {
    string documentContent;
    int choice;
    
    do {
        displayMenu();
        cout << "Enter your choe: ";
        cin >> choice;
        cin.ignore(); // Clear the newline character from the buffer
        switch (choice) {
            case 1:
                createDocument();
                break;
            case 2:
                openDocument(documentContent);
                break;
            case 3:
                editDocument(documentContent);
                break;
            case 4:
                saveDocument(documentContent);
                break;
            case 5:
                cout << "Exiting... Thank you!" << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }
    } while (choice != 5);
    
    return 0;
}
