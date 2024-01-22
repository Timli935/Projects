#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main() {
    //obtain input data and define epsilon
    cout << "Please enter the three side lengths separated by spaces. Example input: \"5 12 13\"\n";
    double x, y, z;
    const double EPSILON = pow(10, -9);
    cin >> x >> y >> z ;
    
    //find the max and min, then find the third side using the total length
    double max_num =max(max(x,y),z);
    double min_num =min(min(x,y),z);
    double sec_num =x+y+z-max_num-min_num;
    
    
    //dislay the sides; setw() used to align the output
    cout << "Largest side: " << setw(8)<< max_num <<"\n";
    cout << "Second largest side: "<< sec_num<<"\n";
    cout << "Smallest side: " << setw(7)<< min_num << "\n";
    //the output may not align correctly if the sides have more than 1 digit
    
    //using algebra to check for right triangle
    cout << boolalpha;
    cout << "Right Triangle: " << (abs(pow(min_num, 2)+pow(sec_num, 2)-pow(max_num, 2))<=EPSILON) << "\n";
    
    return 0;
}
