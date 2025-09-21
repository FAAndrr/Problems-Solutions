#include <iostream>
using namespace std;
int main() {
    int n, x, y;
    string ins;
    cin >> n;
    cin >> ins;
    for(int i = 0; i < n; i++ ){
        if (ins[i] == 'N'){
            y += 1;
        }
        if (ins[i] == 'E'){
            x += 1;
        }
        if (ins[i] == 'S'){
            y -= 1;
        }
        if (ins[i] == 'W'){
            x -= 1;
        }   
    }    
    int num = abs(x) + abs(y);
    cout << num << endl;
    return 0;
}
