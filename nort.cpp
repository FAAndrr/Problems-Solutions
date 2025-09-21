#include <iostream>
using namespace std;

int w;
int h;
int n;

int main() {

    cin >> w >> h;
    if(w%2==0 or h%2==0){
        n = w*h;
    }
    else {
        n = w*h-1;
    } 
    cout << n << endl;
}