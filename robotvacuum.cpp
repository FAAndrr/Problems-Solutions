// Robot Vacuum (-- 2021 Australian Informatics Olympiad)
// Python / C / C++ / Java

#include <iostream>
using namespace std;
int main() {
    int n, x, y;
    string ins;
    cin >> n;
    cin >> ins;
    for(int i = 0; i < n; i++ ){
        if (ins[i] == 'N') y++; 
        if (ins[i] == 'E') x++;
        if (ins[i] == 'S') y--;
        if (ins[i] == 'W') x--;
    }    
    
    int num = abs(x) + abs(y);
    cout << num << endl;
    return 0;
}

// Max time : 0.004s
// Memory : 0.7 MiB
// Results : 100/100
