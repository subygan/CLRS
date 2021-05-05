#include <iostream>

using namespace std;



void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {

    int n[] = {1,2,3,3,4};

    for(int i=0 ; i<5;i+=1) {

       int j = i-1;
       int value = n[i];

       while (j>=0 && n[j]>=value) {
//            shifting to the right
            n[j+1] = n[j];
            j=j-1;
       }
       n[j+1] = value;
    }
    int size = sizeof(n)/sizeof(n[0]);

    printArray(n,size);
}