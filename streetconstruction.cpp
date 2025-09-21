// Street construction (From Australian Informatics Olympiad -- 2018)
// C/C++/Python/Java
// Time and Memory Limits: 1 second, 1 GB
// Medium Question

// The great city of Dubvegas is designing one side of a new street. This street is divided into evenly
// sized chunks of land, each of which will be used for either a house or a park. The city takes great
// pride in both the number of parks that it has, and that no one has to walk far to reach one of their
// wonderful parks.
// In particular, the city calls a group of consecutive houses a ‘block’. The size of a block is the
// number of houses it contains.
// You must determine, given the number of chunks of land on the street and the number of parks
// that will be built, the minimum possible size of the largest block.
// Input
// The only line will contain the number of chunks of land N on the street, followed by the number
// of parks that will be built K.
// Output
// Your program should output the minimum possible size of the largest block on a street with N
// chunks of land, where K parks will be built.
// Sample Input 1
// 3 1
// Sample Output 1
// 1

//vvvvvvvvvvvvvvvv Solution Below vvvvvvvvvvvvvv

#include <iostream>
using namespace std;

int main() {
    int n, k, x;
    cin >> n >> k;
    x = (n-n%(k+1))/(k+1);
    cout << x << endl;
}

// Max time : 0.001s
// Max memory: 0.5MiB
// Score: 100/100