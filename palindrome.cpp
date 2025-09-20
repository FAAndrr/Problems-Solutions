#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
string word;

int main() {
    cin >> n;
    cin >> word;
    vector<char> letters(word.begin(),word.end());
    for(int i = 0; i < n/2 ; i++) {
       int j = n - i - 1;
       letters[j] = letters[i] = min(letters[i], letters[j]);
    }
    string result(letters.begin(), letters.end());
    cout << result << endl;
}
