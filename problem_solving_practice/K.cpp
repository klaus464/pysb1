#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    
    int sum = 0;
    string num = to_string(n);
    while (n !=0){
        sum += pow(n%10, num.length());
        n /= 10;
    }
    
    if(sum == stoi(num))  cout << "Yes";
    else    cout << "No";
    return 0;
}
