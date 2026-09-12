#include <iostream>

using namespace std;

void solve() {
    int n;
    cin >> n;
    int zeros = 0;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        if (a == 0) {
            zeros++;
        }
    }

    // bessie gets ceil n-1/2 turns
    // is equal to n/2 in integer divs

    if (zeros <= n / 2) {
        cout << "Bessie\n";
    } else {
        cout << "Elsie\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}