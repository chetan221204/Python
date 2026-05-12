// #include <iostream>
// using namespace std;

// int main() {
//     int arr[] = {10, 20, 30, 40, 50};

//     int n = sizeof(arr) / sizeof(arr[0]);

//     for (int i = 0; i < n; i++) {
//         int sum = 0;

//         for (int j = i + 1; j < n; j++) {
//             sum += arr[j];
//         }

//         cout << sum << endl;
//     }

//     return 0;
// }


// #include <iostream>
// using namespace std;

// int main() {
//     int arr[] = {10, 20, 30, 40, 50};
//     int sum=0;
//     int n = sizeof(arr) / sizeof(arr[0]);
//     for (int j = 0; j < n; j++) {
//         sum += arr[j];
// }
//     for (int i=0;i<n;i++){
//         sum=sum-arr[i];

//         cout<<sum<<" ";
//     }
// }


#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int j = n-1; j >=0; j--) {
        cout<<j<<" ";
         
}
}