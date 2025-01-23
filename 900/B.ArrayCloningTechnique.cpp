#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t; // Read the number of test cases
    while(t--) {
        int n;
        cin >> n; // Read the number of elements
        vector<int> numbers(n);
        unordered_map<int, int> d;

        for(int i = 0; i < n; i++) {
            cin >> numbers[i];
        }

        int m = 0;
        for(int i : numbers) {
            d[i]++;
            m = max(m, d[i]);
        }

        int count = 0;
        int value = m;
        while (value < n) {
            count++;
            if (2 * value > n) {
                count += n - value;
                break;
            } else {
                count += value;
                value = 2 * value;
            }
        }

        cout << count << endl;
    }

    return 0;
}