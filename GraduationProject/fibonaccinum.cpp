// CPP program to find the Nth term
// of Fibonacci series
#include <iostream>
using namespace std;

unsigned long long int fib(int n, unsigned long long int* term)
{

    // base case
    if (n <= 1)
        return n;

    // if fib(n) has already been computed
    // we do not do further recursive calls
    // and hence reduce the number of repeated
    // work
    if (term[n] != 0)
        return term[n];

    else {

        // store the computed value of fib(n)
        // in an array term at index n to
        // so that it does not needs to be
        // precomputed again
        term[n] = fib((n - 1), term) + fib((n - 2), term);
        return term[n];
    }
}

// Fibonacci Series using memoized Recursion
unsigned long long int mfib(int n) {
    unsigned long long int *term = new unsigned long long int[n+1];
    for (int i = 0; i <= n; i++) {
        term[i] = 0;
    }
    unsigned long long int result = fib(n, term);
    delete[] term;
    return result;
}



// Driver Code
int main()
{
    int n = 91;
    cout << mfib(n);
    return 0;
}