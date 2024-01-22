
#include <iostream>
using namespace std;

int main() {
    //variables for prime number calculation, num_in is the input, num_prime is the final prime number, prime_count is counting the number of prime numbers in the loop
    // if_prime indicates whether it is a prime number
    int num_in;
    int num_prime = 2;
    int prime_count = 0;
    bool if_prime;
    //variables for Fibonacci number
    int x1 = 1;
    int x2 = 1;
    int next;
    int fib_count = 0;
    
    //ask for input
    cout << "Enter a positive integer: ";
    cin >> num_in;
    
    //prime number loops
    //the loop checks if a number is divisible by a number other than itself
    //if it is divisible, i/k would be zero and it is not a prime number
    for (int i = 2; i < INT_MAX; ++i) {
        if_prime = true;
        for(int k = 2; k <= i/2;++k) {
            if (i%k == 0){
                if_prime = false;
                break;
            }
        }
        if(if_prime == true){
            ++prime_count;
            if(prime_count == num_in){
                num_prime = i;
                break;
            }
        }
    }
    
    //Fibonacci number loops
    //the loop will only run if the input is larger than 3
    next = x1 + x2;
    for (int i = 3; i < num_in; ++i){
        x1 = x2;
        x2 = next;
        next = x1 + x2;
        ++fib_count;
    }
    
    //final output for fibonacci number, the if statement considers the occassion where the input is less than 3, in which case the output will be 1
    if (num_in == 1 || num_in == 2) {
        cout << "The " << num_in << "th Fibonacci number is: " << x1 << ". \n";
    }
    else{
        cout << "The " << num_in << "th Fibonacci number is: " << next << ". \n";
    }
    //final output for prime numnber
    cout << "The " << num_in << "th prime number is: " << num_prime << ". \n";
    
    return 0;
}
