// CPP program to find the Nth term
// of Fibonacci series
#include <iostream>
#include "Bigint.h"
using namespace Dodecahedron;

Bigint fib(int n, Bigint* term)
{
    Bigint d;
    d = 0;
    Bigint a;
    // base case
    if (n == 1){
        a = 1;
        return a;
    }
    if (n == 0) {
        a = 0;
        return a;
    }
       

    // if fib(n) has already been computed
    // we do not do further recursive calls
    // and hence reduce the number of repeated
    // work
    if (!(term[n] == d)) {
        return term[n];
    }
        

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
Bigint mfib(int n) {
    Bigint* term = new Bigint[n + 1];
    for (int i = 0; i <= n; i++) {
        term[i] = 0;
    }
    Bigint result = fib(n, term);
    delete[] term;
    return result;
}



// Driver Code
int main()
{
    int n = 110;
    std::cout << mfib(n);
    return 0;
}